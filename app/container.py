from dependency_injector import containers
from dependency_injector import containers, providers
from services import relay

class AppContainer(containers.DeclarativeContainer):
  config = providers.Configuration()
  config.host.from_env('API_HOST')
  config.port.from_env('API_PORT')

  relay_service = providers.Factory(
    relay.RelayService
  )
  