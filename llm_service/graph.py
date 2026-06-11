import warnings

warnings.filterwarnings(  # noqa: E402
    "ignore",
    message=r"The default value of `allowed_objects` will change in a future version.*",
)
warnings.filterwarnings("ignore", module=r"langgraph\.checkpoint\.base.*")  # noqa: E402

from langgraph.graph import StateGraph, START, END  # noqa: E402
from langgraph.prebuilt import ToolNode, tools_condition  # noqa: E402
from typing import Literal  # noqa: E402
from langgraph.graph import MessagesState  # noqa: E402
from langchain_google_genai import ChatGoogleGenerativeAI  # noqa: E402
from pydantic import BaseModel, Field  # noqa: E402
from pathlib import Path  # noqa: E402
import logging  # noqa: E402


logger = logging.getLogger(__name__)
SYSTEM_PROMPT_PATH = Path(__file__).resolve().parent / "system_prompt.txt"


def load_system_prompt() -> str:
    return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8").strip()


class GraphBuilder:
    def __init__(
        self,
        tools,
        llm_model: str = "gemini-flash-lite-latest",
        gemini_api_key: str | None = None,
    ):
        self.tools = tools
        self.llm_model = llm_model
        self.gemini_api_key = gemini_api_key
        self.system_prompt = load_system_prompt()
        self.workflow = StateGraph(MessagesState)
        self._build_graph()

    def _llm(self):
        return ChatGoogleGenerativeAI(
            temperature=0,
            model=self.llm_model,
            google_api_key=self.gemini_api_key,
        )

    def generate_query_or_respond(self, state: MessagesState):
        """Call the model to generate a response based on the current state. Given
        the question, it will decide to retrieve using the retriever tool, or simply respond to the user.
        """
        messages = [{"role": "system", "content": self.system_prompt}, *state["messages"]]
        response = (
            self._llm()
            .bind_tools([self.tools]).invoke(messages)
        )
        return {"messages": [response]}

    def grade_documents(self, state) -> Literal["generate_answer", "rewrite_question"]:
        """Determine whether the retrieved documents are relevant to the question."""

        logger.debug("Checking retrieved document relevance")

        class GradeDocuments(BaseModel):
            """Grade documents using a binary score for relevance check."""
            binary_score: str = Field(
                description="Relevance score: 'yes' if relevant, or 'no' if not relevant"
            )

        question = state["messages"][0].content
        context = state["messages"][-1].content

        GRADE_PROMPT = (
            "You are a grader assessing relevance of a retrieved document to a user question. \n "
            "Here is the retrieved document: \n\n {context} \n\n"
            "Here is the user question: {question} \n"
            "If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n"
            "Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."
        )

        prompt = GRADE_PROMPT.format(question=question, context=context)

        response = (
            self._llm()
            .with_structured_output(GradeDocuments).invoke(
                [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt},
                ]
            )
        )
        score = response.binary_score

        if score == "yes":
            logger.info("Retrieved documents are relevant")
            return "generate_answer"
        else:
            logger.info("Retrieved documents are not relevant")
            return "rewrite_question"

    def rewrite_question(self, state: MessagesState):
        """Rewrite the original user question."""
        REWRITE_PROMPT = (
            "Look at the input and try to reason about the underlying semantic intent / meaning.\n"
            "Here is the initial question:"
            "\n ------- \n"
            "{question}"
            "\n ------- \n"
            "Formulate an improved question:"
        )
        messages = state["messages"]
        question = messages[0].content
        prompt = REWRITE_PROMPT.format(question=question)
        response_model = self._llm()
        response = response_model.invoke(
            [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ]
        )
        return {"messages": [{"role": "user", "content": response.content}]}

    def generate_answer(self, state: MessagesState):
        """Generate an answer."""
        GENERATE_PROMPT = (
            "You are an assistant for question-answering tasks. "
            "Use the following pieces of retrieved context to answer the question. "
            "If you don't know the answer, just say that you don't know. "
            "Use three sentences maximum and keep the answer concise.\n"
            "Question: {question} \n"
            "Context: {context}"
        )
        question = state["messages"][0].content
        context = state["messages"][-1].content
        prompt = GENERATE_PROMPT.format(question=question, context=context)
        response_model = self._llm()
        response = response_model.invoke(
            [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
            ]
        )
        return {"messages": [response]}

    def _build_graph(self):
        self.workflow.add_node(self.generate_query_or_respond)
        self.workflow.add_node("retrieve", ToolNode([self.tools]))
        self.workflow.add_node(self.rewrite_question)
        self.workflow.add_node(self.generate_answer)

        self.workflow.add_edge(START, "generate_query_or_respond")

        self.workflow.add_conditional_edges(
            "generate_query_or_respond",
            tools_condition,
            {
                "tools": "retrieve",
                END: END,
            },
        )
        self.workflow.add_conditional_edges(
            "retrieve",
            self.grade_documents,
        )
        self.workflow.add_edge("generate_answer", END)
        self.workflow.add_edge("rewrite_question", "generate_query_or_respond")

    def compile(self):
        return self.workflow.compile()
