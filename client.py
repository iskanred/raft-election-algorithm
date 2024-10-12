import grpc
import raft_pb2
import sys

from raft_pb2_grpc import RaftElectionServiceStub as RaftElectionService
from typing import Optional

AppendRequest = raft_pb2.AppendRequest
AppendResponse = raft_pb2.AppendResponse
GetLeaderResponse = raft_pb2.GetLeaderResponse
SuspendRequest = raft_pb2.SuspendRequest
Void = raft_pb2.Void
VoteRequest = raft_pb2.VoteRequest
VoteResponse = raft_pb2.VoteResponse
Key = raft_pb2.Key
KeyValue = raft_pb2.KeyValue
SetValResponse = raft_pb2.SetValResponse
GetValResponse = raft_pb2.GetValResponse


class CommandNotExistError(Exception):
    pass


class NoServerProvidedError(Exception):
    pass


class InternalSerivceError(Exception):
    pass


class UserService:

    def __init__(self):
        self.address: Optional[str] = None
        self.service: Optional[RaftElectionService] = None

    def connect(self, ipaddr: str, port: int) -> None:
        self.address = f"{ipaddr}:{port}"
        channel = grpc.insecure_channel(self.address)
        self.service = RaftElectionService(channel)

    def get_leader(self) -> (int, str):
        self.__validate_server()
        request = Void()
        response: GetLeaderResponse = self.service.GetLeader(request)
        return response.nodeId, response.nodeAddress

    def suspend(self, period_sec: str) -> None:
        period = self.__validate_period(period_sec)
        self.__validate_server()
        request = SuspendRequest(period=period)
        self.service.Suspend(request)

    def set_val(self, key: str, value: str) -> None:
        self.__validate_server()
        request = KeyValue(key=key, value=value)
        response: SetValResponse = self.service.SetVal(request)
        if not response.success:
            raise InternalSerivceError("Procedure call is failed")

    def get_val(self, key: str) -> Optional[str]:
        self.__validate_server()
        request = Key(key=key)
        response: GetValResponse = self.service.GetVal(request)
        return response.value if response.success else None

    def __validate_server(self):
        if not self.service:
            raise NoServerProvidedError("No server address provided")

    @staticmethod
    def __validate_period(period: str) -> int:
        period = int(period)
        if type(period) is not int or 0 < period > 3600:
            raise ValueError("Period must an integer that belongs to range [0, 3600]")
        return period


def main() -> None:
    service = UserService()
    print("The client starts")

    while True:
        try:
            line = input('> ')
            if not line:
                continue

            command, *args = line.split(maxsplit=1)

            if command == "connect":
                service.connect(*args[0].split(maxsplit=1))
            elif command == "getleader":
                response = service.get_leader()
                print(*response)
            elif command == "suspend":
                service.suspend(period_sec=args[0])
            elif command == "setval":
                key, value = args[0].split(maxsplit=1)
                service.set_val(key=key, value=value)
            elif command == "getval":
                response = service.get_val(key=args[0])
                print(response)
            elif command == "quit":
                raise KeyboardInterrupt
            else:
                raise CommandNotExistError("Command does not exist")
        except grpc.RpcError:
            print("The server is unavailable")
        except KeyboardInterrupt:
            print("The client ends")
            sys.exit(0)
        except InternalSerivceError:
            pass
        except Exception as e:
            print(e)
            print("Try again!")


if __name__ == "__main__":
    main()
