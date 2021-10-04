# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/core/client/v1/client.proto, ibc/core/client/v1/genesis.proto, ibc/core/client/v1/query.proto, ibc/core/client/v1/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class IdentifiedClientState(betterproto.Message):
    """
    IdentifiedClientState defines a client state with an additional client
    identifier field.
    """

    # client identifier
    client_id: str = betterproto.string_field(1)
    # client state
    client_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class ConsensusStateWithHeight(betterproto.Message):
    """
    ConsensusStateWithHeight defines a consensus state with an additional
    height field.
    """

    # consensus state height
    height: "Height" = betterproto.message_field(1)
    # consensus state
    consensus_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        2
    )


@dataclass(eq=False, repr=False)
class ClientConsensusStates(betterproto.Message):
    """
    ClientConsensusStates defines all the stored consensus states for a given
    client.
    """

    # client identifier
    client_id: str = betterproto.string_field(1)
    # consensus states and their heights associated with the client
    consensus_states: List["ConsensusStateWithHeight"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class ClientUpdateProposal(betterproto.Message):
    """
    ClientUpdateProposal is a governance proposal. If it passes, the substitute
    client's latest consensus state is copied over to the subject client. The
    proposal handler may fail if the subject and the substitute do not match in
    client and chain parameters (with exception to latest height, frozen
    height, and chain-id).
    """

    # the title of the update proposal
    title: str = betterproto.string_field(1)
    # the description of the proposal
    description: str = betterproto.string_field(2)
    # the client identifier for the client to be updated if the proposal passes
    subject_client_id: str = betterproto.string_field(3)
    # the substitute client identifier for the client standing in for the subject
    # client
    substitute_client_id: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class UpgradeProposal(betterproto.Message):
    """
    UpgradeProposal is a gov Content type for initiating an IBC breaking
    upgrade.
    """

    title: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)
    plan: "____cosmos_upgrade_v1_beta1__.Plan" = betterproto.message_field(3)
    # An UpgradedClientState must be provided to perform an IBC breaking upgrade.
    # This will make the chain commit to the correct upgraded (self) client state
    # before the upgrade occurs, so that connecting chains can verify that the
    # new upgraded client is valid by verifying a proof on the previous version
    # of the chain. This will allow IBC connections to persist smoothly across
    # planned chain upgrades
    upgraded_client_state: "betterproto_lib_google_protobuf.Any" = (
        betterproto.message_field(4)
    )


@dataclass(eq=False, repr=False)
class Height(betterproto.Message):
    """
    Height is a monotonically increasing data type that can be compared against
    another Height for the purposes of updating and freezing clients Normally
    the RevisionHeight is incremented at each height while keeping
    RevisionNumber the same. However some consensus algorithms may choose to
    reset the height in certain conditions e.g. hard forks, state-machine
    breaking changes In these cases, the RevisionNumber is incremented so that
    height continues to be monitonically increasing even as the RevisionHeight
    gets reset
    """

    # the revision that the client is currently on
    revision_number: int = betterproto.uint64_field(1)
    # the height within the given revision
    revision_height: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the set of IBC light client parameters."""

    # allowed_clients defines the list of allowed client state types.
    allowed_clients: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the ibc client submodule's genesis state."""

    # client states with their corresponding identifiers
    clients: List["IdentifiedClientState"] = betterproto.message_field(1)
    # consensus states from each client
    clients_consensus: List["ClientConsensusStates"] = betterproto.message_field(2)
    # metadata from each client
    clients_metadata: List["IdentifiedGenesisMetadata"] = betterproto.message_field(3)
    params: "Params" = betterproto.message_field(4)
    # create localhost on initialization
    create_localhost: bool = betterproto.bool_field(5)
    # the sequence for the next generated client identifier
    next_client_sequence: int = betterproto.uint64_field(6)


@dataclass(eq=False, repr=False)
class GenesisMetadata(betterproto.Message):
    """
    GenesisMetadata defines the genesis type for metadata that clients may
    return with ExportMetadata
    """

    # store key of metadata without clientID-prefix
    key: bytes = betterproto.bytes_field(1)
    # metadata value
    value: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class IdentifiedGenesisMetadata(betterproto.Message):
    """
    IdentifiedGenesisMetadata has the client metadata with the corresponding
    client id.
    """

    client_id: str = betterproto.string_field(1)
    client_metadata: List["GenesisMetadata"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class QueryClientStateRequest(betterproto.Message):
    """
    QueryClientStateRequest is the request type for the Query/ClientState RPC
    method
    """

    # client state unique identifier
    client_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryClientStateResponse(betterproto.Message):
    """
    QueryClientStateResponse is the response type for the Query/ClientState RPC
    method. Besides the client state, it includes a proof and the height from
    which the proof was retrieved.
    """

    # client state associated with the request identifier
    client_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)
    # merkle proof of existence
    proof: bytes = betterproto.bytes_field(2)
    # height at which the proof was retrieved
    proof_height: "Height" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class QueryClientStatesRequest(betterproto.Message):
    """
    QueryClientStatesRequest is the request type for the Query/ClientStates RPC
    method
    """

    # pagination request
    pagination: "____cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )


@dataclass(eq=False, repr=False)
class QueryClientStatesResponse(betterproto.Message):
    """
    QueryClientStatesResponse is the response type for the Query/ClientStates
    RPC method.
    """

    # list of stored ClientStates of the chain.
    client_states: List["IdentifiedClientState"] = betterproto.message_field(1)
    # pagination response
    pagination: "____cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )


@dataclass(eq=False, repr=False)
class QueryConsensusStateRequest(betterproto.Message):
    """
    QueryConsensusStateRequest is the request type for the Query/ConsensusState
    RPC method. Besides the consensus state, it includes a proof and the height
    from which the proof was retrieved.
    """

    # client identifier
    client_id: str = betterproto.string_field(1)
    # consensus state revision number
    revision_number: int = betterproto.uint64_field(2)
    # consensus state revision height
    revision_height: int = betterproto.uint64_field(3)
    # latest_height overrrides the height field and queries the latest stored
    # ConsensusState
    latest_height: bool = betterproto.bool_field(4)


@dataclass(eq=False, repr=False)
class QueryConsensusStateResponse(betterproto.Message):
    """
    QueryConsensusStateResponse is the response type for the
    Query/ConsensusState RPC method
    """

    # consensus state associated with the client identifier at the given height
    consensus_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        1
    )
    # merkle proof of existence
    proof: bytes = betterproto.bytes_field(2)
    # height at which the proof was retrieved
    proof_height: "Height" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class QueryConsensusStatesRequest(betterproto.Message):
    """
    QueryConsensusStatesRequest is the request type for the
    Query/ConsensusStates RPC method.
    """

    # client identifier
    client_id: str = betterproto.string_field(1)
    # pagination request
    pagination: "____cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(2)
    )


@dataclass(eq=False, repr=False)
class QueryConsensusStatesResponse(betterproto.Message):
    """
    QueryConsensusStatesResponse is the response type for the
    Query/ConsensusStates RPC method
    """

    # consensus states associated with the identifier
    consensus_states: List["ConsensusStateWithHeight"] = betterproto.message_field(1)
    # pagination response
    pagination: "____cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )


@dataclass(eq=False, repr=False)
class QueryClientStatusRequest(betterproto.Message):
    """
    QueryClientStatusRequest is the request type for the Query/ClientStatus RPC
    method
    """

    # client unique identifier
    client_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryClientStatusResponse(betterproto.Message):
    """
    QueryClientStatusResponse is the response type for the Query/ClientStatus
    RPC method. It returns the current status of the IBC client.
    """

    status: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryClientParamsRequest(betterproto.Message):
    """
    QueryClientParamsRequest is the request type for the Query/ClientParams RPC
    method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryClientParamsResponse(betterproto.Message):
    """
    QueryClientParamsResponse is the response type for the Query/ClientParams
    RPC method.
    """

    # params defines the parameters of the module.
    params: "Params" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryUpgradedClientStateRequest(betterproto.Message):
    """
    QueryUpgradedClientStateRequest is the request type for the
    Query/UpgradedClientState RPC method
    """

    pass


@dataclass(eq=False, repr=False)
class QueryUpgradedClientStateResponse(betterproto.Message):
    """
    QueryUpgradedClientStateResponse is the response type for the
    Query/UpgradedClientState RPC method.
    """

    # client state associated with the request identifier
    upgraded_client_state: "betterproto_lib_google_protobuf.Any" = (
        betterproto.message_field(1)
    )


@dataclass(eq=False, repr=False)
class QueryUpgradedConsensusStateRequest(betterproto.Message):
    """
    QueryUpgradedConsensusStateRequest is the request type for the
    Query/UpgradedConsensusState RPC method
    """

    pass


@dataclass(eq=False, repr=False)
class QueryUpgradedConsensusStateResponse(betterproto.Message):
    """
    QueryUpgradedConsensusStateResponse is the response type for the
    Query/UpgradedConsensusState RPC method.
    """

    # Consensus state associated with the request identifier
    upgraded_consensus_state: "betterproto_lib_google_protobuf.Any" = (
        betterproto.message_field(1)
    )


@dataclass(eq=False, repr=False)
class MsgCreateClient(betterproto.Message):
    """MsgCreateClient defines a message to create an IBC client"""

    # light client state
    client_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)
    # consensus state associated with the client that corresponds to a given
    # height.
    consensus_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        2
    )
    # signer address
    signer: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgCreateClientResponse(betterproto.Message):
    """MsgCreateClientResponse defines the Msg/CreateClient response type."""

    pass


@dataclass(eq=False, repr=False)
class MsgUpdateClient(betterproto.Message):
    """
    MsgUpdateClient defines an sdk.Msg to update a IBC client state using the
    given header.
    """

    # client unique identifier
    client_id: str = betterproto.string_field(1)
    # header to update the light client
    header: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)
    # signer address
    signer: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgUpdateClientResponse(betterproto.Message):
    """MsgUpdateClientResponse defines the Msg/UpdateClient response type."""

    pass


@dataclass(eq=False, repr=False)
class MsgUpgradeClient(betterproto.Message):
    """
    MsgUpgradeClient defines an sdk.Msg to upgrade an IBC client to a new
    client state
    """

    # client unique identifier
    client_id: str = betterproto.string_field(1)
    # upgraded client state
    client_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)
    # upgraded consensus state, only contains enough information to serve as a
    # basis of trust in update logic
    consensus_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        3
    )
    # proof that old chain committed to new client
    proof_upgrade_client: bytes = betterproto.bytes_field(4)
    # proof that old chain committed to new consensus state
    proof_upgrade_consensus_state: bytes = betterproto.bytes_field(5)
    # signer address
    signer: str = betterproto.string_field(6)


@dataclass(eq=False, repr=False)
class MsgUpgradeClientResponse(betterproto.Message):
    """
    MsgUpgradeClientResponse defines the Msg/UpgradeClient response type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgSubmitMisbehaviour(betterproto.Message):
    """
    MsgSubmitMisbehaviour defines an sdk.Msg type that submits Evidence for
    light client misbehaviour.
    """

    # client unique identifier
    client_id: str = betterproto.string_field(1)
    # misbehaviour used for freezing the light client
    misbehaviour: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)
    # signer address
    signer: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgSubmitMisbehaviourResponse(betterproto.Message):
    """
    MsgSubmitMisbehaviourResponse defines the Msg/SubmitMisbehaviour response
    type.
    """

    pass


class QueryStub(betterproto.ServiceStub):
    async def client_state(self, *, client_id: str = "") -> "QueryClientStateResponse":

        request = QueryClientStateRequest()
        request.client_id = client_id

        return await self._unary_unary(
            "/ibc.core.client.v1.Query/ClientState", request, QueryClientStateResponse
        )

    async def client_states(
        self, *, pagination: "____cosmos_base_query_v1_beta1__.PageRequest" = None
    ) -> "QueryClientStatesResponse":

        request = QueryClientStatesRequest()
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/ibc.core.client.v1.Query/ClientStates", request, QueryClientStatesResponse
        )

    async def consensus_state(
        self,
        *,
        client_id: str = "",
        revision_number: int = 0,
        revision_height: int = 0,
        latest_height: bool = False,
    ) -> "QueryConsensusStateResponse":

        request = QueryConsensusStateRequest()
        request.client_id = client_id
        request.revision_number = revision_number
        request.revision_height = revision_height
        request.latest_height = latest_height

        return await self._unary_unary(
            "/ibc.core.client.v1.Query/ConsensusState",
            request,
            QueryConsensusStateResponse,
        )

    async def consensus_states(
        self,
        *,
        client_id: str = "",
        pagination: "____cosmos_base_query_v1_beta1__.PageRequest" = None,
    ) -> "QueryConsensusStatesResponse":

        request = QueryConsensusStatesRequest()
        request.client_id = client_id
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/ibc.core.client.v1.Query/ConsensusStates",
            request,
            QueryConsensusStatesResponse,
        )

    async def client_status(
        self, *, client_id: str = ""
    ) -> "QueryClientStatusResponse":

        request = QueryClientStatusRequest()
        request.client_id = client_id

        return await self._unary_unary(
            "/ibc.core.client.v1.Query/ClientStatus", request, QueryClientStatusResponse
        )

    async def client_params(self) -> "QueryClientParamsResponse":

        request = QueryClientParamsRequest()

        return await self._unary_unary(
            "/ibc.core.client.v1.Query/ClientParams", request, QueryClientParamsResponse
        )

    async def upgraded_client_state(self) -> "QueryUpgradedClientStateResponse":

        request = QueryUpgradedClientStateRequest()

        return await self._unary_unary(
            "/ibc.core.client.v1.Query/UpgradedClientState",
            request,
            QueryUpgradedClientStateResponse,
        )

    async def upgraded_consensus_state(self) -> "QueryUpgradedConsensusStateResponse":

        request = QueryUpgradedConsensusStateRequest()

        return await self._unary_unary(
            "/ibc.core.client.v1.Query/UpgradedConsensusState",
            request,
            QueryUpgradedConsensusStateResponse,
        )


class MsgStub(betterproto.ServiceStub):
    async def create_client(
        self,
        *,
        client_state: "betterproto_lib_google_protobuf.Any" = None,
        consensus_state: "betterproto_lib_google_protobuf.Any" = None,
        signer: str = "",
    ) -> "MsgCreateClientResponse":

        request = MsgCreateClient()
        if client_state is not None:
            request.client_state = client_state
        if consensus_state is not None:
            request.consensus_state = consensus_state
        request.signer = signer

        return await self._unary_unary(
            "/ibc.core.client.v1.Msg/CreateClient", request, MsgCreateClientResponse
        )

    async def update_client(
        self,
        *,
        client_id: str = "",
        header: "betterproto_lib_google_protobuf.Any" = None,
        signer: str = "",
    ) -> "MsgUpdateClientResponse":

        request = MsgUpdateClient()
        request.client_id = client_id
        if header is not None:
            request.header = header
        request.signer = signer

        return await self._unary_unary(
            "/ibc.core.client.v1.Msg/UpdateClient", request, MsgUpdateClientResponse
        )

    async def upgrade_client(
        self,
        *,
        client_id: str = "",
        client_state: "betterproto_lib_google_protobuf.Any" = None,
        consensus_state: "betterproto_lib_google_protobuf.Any" = None,
        proof_upgrade_client: bytes = b"",
        proof_upgrade_consensus_state: bytes = b"",
        signer: str = "",
    ) -> "MsgUpgradeClientResponse":

        request = MsgUpgradeClient()
        request.client_id = client_id
        if client_state is not None:
            request.client_state = client_state
        if consensus_state is not None:
            request.consensus_state = consensus_state
        request.proof_upgrade_client = proof_upgrade_client
        request.proof_upgrade_consensus_state = proof_upgrade_consensus_state
        request.signer = signer

        return await self._unary_unary(
            "/ibc.core.client.v1.Msg/UpgradeClient", request, MsgUpgradeClientResponse
        )

    async def submit_misbehaviour(
        self,
        *,
        client_id: str = "",
        misbehaviour: "betterproto_lib_google_protobuf.Any" = None,
        signer: str = "",
    ) -> "MsgSubmitMisbehaviourResponse":

        request = MsgSubmitMisbehaviour()
        request.client_id = client_id
        if misbehaviour is not None:
            request.misbehaviour = misbehaviour
        request.signer = signer

        return await self._unary_unary(
            "/ibc.core.client.v1.Msg/SubmitMisbehaviour",
            request,
            MsgSubmitMisbehaviourResponse,
        )


class QueryBase(ServiceBase):
    async def client_state(self, client_id: str) -> "QueryClientStateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def client_states(
        self, pagination: "____cosmos_base_query_v1_beta1__.PageRequest"
    ) -> "QueryClientStatesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def consensus_state(
        self,
        client_id: str,
        revision_number: int,
        revision_height: int,
        latest_height: bool,
    ) -> "QueryConsensusStateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def consensus_states(
        self, client_id: str, pagination: "____cosmos_base_query_v1_beta1__.PageRequest"
    ) -> "QueryConsensusStatesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def client_status(self, client_id: str) -> "QueryClientStatusResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def client_params(self) -> "QueryClientParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def upgraded_client_state(self) -> "QueryUpgradedClientStateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def upgraded_consensus_state(self) -> "QueryUpgradedConsensusStateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_client_state(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "client_id": request.client_id,
        }

        response = await self.client_state(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_client_states(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "pagination": request.pagination,
        }

        response = await self.client_states(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_consensus_state(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "client_id": request.client_id,
            "revision_number": request.revision_number,
            "revision_height": request.revision_height,
            "latest_height": request.latest_height,
        }

        response = await self.consensus_state(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_consensus_states(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "client_id": request.client_id,
            "pagination": request.pagination,
        }

        response = await self.consensus_states(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_client_status(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "client_id": request.client_id,
        }

        response = await self.client_status(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_client_params(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.client_params(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_upgraded_client_state(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.upgraded_client_state(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_upgraded_consensus_state(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.upgraded_consensus_state(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ibc.core.client.v1.Query/ClientState": grpclib.const.Handler(
                self.__rpc_client_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryClientStateRequest,
                QueryClientStateResponse,
            ),
            "/ibc.core.client.v1.Query/ClientStates": grpclib.const.Handler(
                self.__rpc_client_states,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryClientStatesRequest,
                QueryClientStatesResponse,
            ),
            "/ibc.core.client.v1.Query/ConsensusState": grpclib.const.Handler(
                self.__rpc_consensus_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConsensusStateRequest,
                QueryConsensusStateResponse,
            ),
            "/ibc.core.client.v1.Query/ConsensusStates": grpclib.const.Handler(
                self.__rpc_consensus_states,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConsensusStatesRequest,
                QueryConsensusStatesResponse,
            ),
            "/ibc.core.client.v1.Query/ClientStatus": grpclib.const.Handler(
                self.__rpc_client_status,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryClientStatusRequest,
                QueryClientStatusResponse,
            ),
            "/ibc.core.client.v1.Query/ClientParams": grpclib.const.Handler(
                self.__rpc_client_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryClientParamsRequest,
                QueryClientParamsResponse,
            ),
            "/ibc.core.client.v1.Query/UpgradedClientState": grpclib.const.Handler(
                self.__rpc_upgraded_client_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryUpgradedClientStateRequest,
                QueryUpgradedClientStateResponse,
            ),
            "/ibc.core.client.v1.Query/UpgradedConsensusState": grpclib.const.Handler(
                self.__rpc_upgraded_consensus_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryUpgradedConsensusStateRequest,
                QueryUpgradedConsensusStateResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def create_client(
        self,
        client_state: "betterproto_lib_google_protobuf.Any",
        consensus_state: "betterproto_lib_google_protobuf.Any",
        signer: str,
    ) -> "MsgCreateClientResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def update_client(
        self, client_id: str, header: "betterproto_lib_google_protobuf.Any", signer: str
    ) -> "MsgUpdateClientResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def upgrade_client(
        self,
        client_id: str,
        client_state: "betterproto_lib_google_protobuf.Any",
        consensus_state: "betterproto_lib_google_protobuf.Any",
        proof_upgrade_client: bytes,
        proof_upgrade_consensus_state: bytes,
        signer: str,
    ) -> "MsgUpgradeClientResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def submit_misbehaviour(
        self,
        client_id: str,
        misbehaviour: "betterproto_lib_google_protobuf.Any",
        signer: str,
    ) -> "MsgSubmitMisbehaviourResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_create_client(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "client_state": request.client_state,
            "consensus_state": request.consensus_state,
            "signer": request.signer,
        }

        response = await self.create_client(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_update_client(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "client_id": request.client_id,
            "header": request.header,
            "signer": request.signer,
        }

        response = await self.update_client(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_upgrade_client(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "client_id": request.client_id,
            "client_state": request.client_state,
            "consensus_state": request.consensus_state,
            "proof_upgrade_client": request.proof_upgrade_client,
            "proof_upgrade_consensus_state": request.proof_upgrade_consensus_state,
            "signer": request.signer,
        }

        response = await self.upgrade_client(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_submit_misbehaviour(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "client_id": request.client_id,
            "misbehaviour": request.misbehaviour,
            "signer": request.signer,
        }

        response = await self.submit_misbehaviour(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ibc.core.client.v1.Msg/CreateClient": grpclib.const.Handler(
                self.__rpc_create_client,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgCreateClient,
                MsgCreateClientResponse,
            ),
            "/ibc.core.client.v1.Msg/UpdateClient": grpclib.const.Handler(
                self.__rpc_update_client,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpdateClient,
                MsgUpdateClientResponse,
            ),
            "/ibc.core.client.v1.Msg/UpgradeClient": grpclib.const.Handler(
                self.__rpc_upgrade_client,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpgradeClient,
                MsgUpgradeClientResponse,
            ),
            "/ibc.core.client.v1.Msg/SubmitMisbehaviour": grpclib.const.Handler(
                self.__rpc_submit_misbehaviour,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSubmitMisbehaviour,
                MsgSubmitMisbehaviourResponse,
            ),
        }


from .....cosmos.base.query import v1beta1 as ____cosmos_base_query_v1_beta1__
from .....cosmos.upgrade import v1beta1 as ____cosmos_upgrade_v1_beta1__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
