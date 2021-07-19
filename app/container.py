from dependency_injector import containers
from dependency_injector import containers, providers
from services import relay, serial

class AppContainer(containers.DeclarativeContainer):
  config = providers.Configuration()
  config.host.from_env('API_HOST')
  config.port.from_env('API_PORT')
  config.serial_port.from_env('SERIAL_PORT')

  serial_service = providers.Singleton(
    serial.SerialComService,
    serial_port=config.serial_port
  )

  relay_service = providers.Singleton(
    relay.RelayService,
    serial_service=serial_service
  )
