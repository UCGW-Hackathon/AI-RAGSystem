// ─────────────────────────────────────────────────────────────────────────────
// azure/container-apps.bicep
// Production-grade Azure Container Apps deployment for AI-RAGSystem
// Uses GitHub Container Registry (GHCR) — compatible with Azure for Students
// ─────────────────────────────────────────────────────────────────────────────

@description('Base name used to derive all resource names')
param appName string = 'ragrag'

@description('Azure region')
param location string = resourceGroup().location

@description('Full API image URI including tag (e.g. ghcr.io/user/ragrag-api:abc1234)')
param apiImage string

@description('Full Worker image URI including tag')
param workerImage string

@description('Image tag — used for display only')
param imageTag string = 'latest'

@description('Container registry server (ghcr.io)')
param registryServer string = 'ghcr.io'

@description('Registry username (GitHub username)')
param registryUsername string

@description('Registry password (GitHub PAT with read:packages scope)')
@secure()
param registryPassword string

// ── App secrets ───────────────────────────────────────────────────────────────
@secure()
param geminiApiKey string

@secure()
param qdrantUrl string

@secure()
param qdrantApiKey string

@secure()
param cloudAmqpUrl string

// ── App config ────────────────────────────────────────────────────────────────
param llmModel string = 'gemini-flash-lite-latest'
param collectionName string = 'my_collection'
param embeddingsModel string = 'sentence-transformers/all-MiniLM-L6-v2'
param logLevel string = 'INFO'
param allowedOrigins string = '*'
param minReplicas int = 1
param maxReplicas int = 3


// ─────────────────────────────────────────────────────────────────────────────
// Variables
// ─────────────────────────────────────────────────────────────────────────────
var logAnalyticsName = '${appName}-logs'
var environmentName = '${appName}-env'
var apiAppName = '${appName}-api'
var workerAppName = '${appName}-worker'


// ─────────────────────────────────────────────────────────────────────────────
// Log Analytics Workspace
// ─────────────────────────────────────────────────────────────────────────────
resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: logAnalyticsName
  location: location
  properties: {
    sku: { name: 'PerGB2018' }
    retentionInDays: 30
    features: { enableLogAccessUsingOnlyResourcePermissions: true }
  }
}


// ─────────────────────────────────────────────────────────────────────────────
// Container Apps Environment
// ─────────────────────────────────────────────────────────────────────────────
resource environment 'Microsoft.App/managedEnvironments@2023-05-01' = {
  name: environmentName
  location: location
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: logAnalytics.properties.customerId
        sharedKey: logAnalytics.listKeys().primarySharedKey
      }
    }
  }
}


// ─────────────────────────────────────────────────────────────────────────────
// Shared secrets and environment variables
// ─────────────────────────────────────────────────────────────────────────────
var sharedSecrets = [
  { name: 'gemini-api-key',   value: geminiApiKey }
  { name: 'qdrant-url',       value: qdrantUrl }
  { name: 'qdrant-api-key',   value: qdrantApiKey }
  { name: 'cloudamqp-url',    value: cloudAmqpUrl }
  { name: 'registry-password', value: registryPassword }
]

var sharedEnvVars = [
  { name: 'GEMINI_API_KEY',   secretRef: 'gemini-api-key' }
  { name: 'QDRANT_URL',       secretRef: 'qdrant-url' }
  { name: 'QDRANT_API_KEY',   secretRef: 'qdrant-api-key' }
  { name: 'CLOUDAMQP_URL',    secretRef: 'cloudamqp-url' }
  { name: 'LLM_MODEL',        value: llmModel }
  { name: 'COLLECTION_NAME',  value: collectionName }
  { name: 'EMBEDDINGS_MODEL', value: embeddingsModel }
  { name: 'LOG_LEVEL',        value: logLevel }
  { name: 'USER_AGENT',       value: 'SiTukang-RAG/1.0' }
]

var registryConfig = [
  {
    server:            registryServer
    username:          registryUsername
    passwordSecretRef: 'registry-password'
  }
]


// ─────────────────────────────────────────────────────────────────────────────
// Container App: llm-service (FastAPI API)
// ─────────────────────────────────────────────────────────────────────────────
resource apiApp 'Microsoft.App/containerApps@2023-05-01' = {
  name: apiAppName
  location: location
  properties: {
    managedEnvironmentId: environment.id
    configuration: {
      activeRevisionsMode: 'Single'
      secrets:    sharedSecrets
      registries: registryConfig
      ingress: {
        external:   true
        targetPort: 8001
        transport:  'http'
        corsPolicy: {
          allowedOrigins:   split(allowedOrigins, ',')
          allowedMethods:   ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
          allowedHeaders:   ['*']
          allowCredentials: true
        }
      }
    }
    template: {
      containers: [
        {
          name:  'llm-service'
          image: apiImage
          env: concat(sharedEnvVars, [
            { name: 'ALLOWED_ORIGINS', value: allowedOrigins }
            { name: 'DOCUMENTS_DIR',   value: '/app/documents' }
          ])
          resources: {
            cpu:    '1.0'
            memory: '2Gi'
          }
          probes: [
            {
              type: 'Liveness'
              httpGet: { path: '/health', port: 8001, scheme: 'HTTP' }
              initialDelaySeconds: 60
              periodSeconds:       30
              failureThreshold:    3
            }
            {
              type: 'Readiness'
              httpGet: { path: '/health', port: 8001, scheme: 'HTTP' }
              initialDelaySeconds: 30
              periodSeconds:       10
              failureThreshold:    5
            }
          ]
        }
      ]
      scale: {
        minReplicas: minReplicas
        maxReplicas: maxReplicas
        rules: [
          {
            name: 'http-scaling'
            http: { metadata: { concurrentRequests: '20' } }
          }
        ]
      }
    }
  }
}


// ─────────────────────────────────────────────────────────────────────────────
// Container App: rag-worker (AMQP consumer)
// ─────────────────────────────────────────────────────────────────────────────
resource workerApp 'Microsoft.App/containerApps@2023-05-01' = {
  name: workerAppName
  location: location
  properties: {
    managedEnvironmentId: environment.id
    configuration: {
      activeRevisionsMode: 'Single'
      secrets:    sharedSecrets
      registries: registryConfig
      // No ingress — worker is internal only
    }
    template: {
      containers: [
        {
          name:  'rag-worker'
          image: workerImage
          env: concat(sharedEnvVars, [
            { name: 'AMQP_QUEUE_INJECT',    value: 'rag.inject' }
            { name: 'AMQP_EXCHANGE',         value: 'rag' }
            { name: 'WORKER_PREFETCH_COUNT', value: '1' }
            { name: 'WORKER_MAX_RETRIES',    value: '3' }
            { name: 'DOCUMENTS_DIR',         value: '/app/documents' }
          ])
          resources: {
            cpu:    '0.5'
            memory: '1Gi'
          }
        }
      ]
      scale: {
        minReplicas: 1
        maxReplicas: 2
      }
    }
  }
}


// ─────────────────────────────────────────────────────────────────────────────
// Outputs
// ─────────────────────────────────────────────────────────────────────────────
output apiUrl string = 'https://${apiApp.properties.configuration.ingress.fqdn}'
output apiAppName string = apiApp.name
output workerAppName string = workerApp.name
output environmentName string = environment.name
