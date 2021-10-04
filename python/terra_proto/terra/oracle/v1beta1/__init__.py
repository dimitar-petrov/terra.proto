# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: terra/oracle/v1beta1/genesis.proto, terra/oracle/v1beta1/oracle.proto, terra/oracle/v1beta1/query.proto, terra/oracle/v1beta1/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the parameters for the oracle module."""

    vote_period: int = betterproto.uint64_field(1)
    vote_threshold: str = betterproto.string_field(2)
    reward_band: str = betterproto.string_field(3)
    reward_distribution_window: int = betterproto.uint64_field(4)
    whitelist: List["Denom"] = betterproto.message_field(5)
    slash_fraction: str = betterproto.string_field(6)
    slash_window: int = betterproto.uint64_field(7)
    min_valid_per_window: str = betterproto.string_field(8)


@dataclass(eq=False, repr=False)
class Denom(betterproto.Message):
    """Denom - the object to hold configurations of each denom"""

    name: str = betterproto.string_field(1)
    tobin_tax: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class AggregateExchangeRatePrevote(betterproto.Message):
    """
    struct for aggregate prevoting on the ExchangeRateVote. The purpose of
    aggregate prevote is to hide vote exchange rates with hash which is
    formatted as hex string in SHA256("{salt}:{exchange
    rate}{denom},...,{exchange rate}{denom}:{voter}")
    """

    hash: str = betterproto.string_field(1)
    voter: str = betterproto.string_field(2)
    submit_block: int = betterproto.uint64_field(3)


@dataclass(eq=False, repr=False)
class AggregateExchangeRateVote(betterproto.Message):
    """
    MsgAggregateExchangeRateVote - struct for voting on the exchange rates of
    Luna denominated in various Terra assets.
    """

    exchange_rate_tuples: List["ExchangeRateTuple"] = betterproto.message_field(1)
    voter: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ExchangeRateTuple(betterproto.Message):
    """
    ExchangeRateTuple - struct to store interpreted exchange rates data to
    store
    """

    denom: str = betterproto.string_field(1)
    exchange_rate: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class QueryExchangeRateRequest(betterproto.Message):
    """
    QueryExchangeRateRequest is the request type for the Query/ExchangeRate RPC
    method.
    """

    # denom defines the denomination to query for.
    denom: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryExchangeRateResponse(betterproto.Message):
    """
    QueryExchangeRateResponse is response type for the Query/ExchangeRate RPC
    method.
    """

    # exchange_rate defines the exchange rate of Luna denominated in various
    # Terra
    exchange_rate: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryExchangeRatesRequest(betterproto.Message):
    """
    QueryExchangeRatesRequest is the request type for the Query/ExchangeRates
    RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryExchangeRatesResponse(betterproto.Message):
    """
    QueryExchangeRatesResponse is response type for the Query/ExchangeRates RPC
    method.
    """

    # exchange_rates defines a list of the exchange rate for all whitelisted
    # denoms.
    exchange_rates: List[
        "___cosmos_base_v1_beta1__.DecCoin"
    ] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryTobinTaxRequest(betterproto.Message):
    """
    QueryTobinTaxRequest is the request type for the Query/TobinTax RPC method.
    """

    # denom defines the denomination to query for.
    denom: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryTobinTaxResponse(betterproto.Message):
    """
    QueryTobinTaxResponse is response type for the Query/TobinTax RPC method.
    """

    # tobin_taxe defines the tobin tax of a denom
    tobin_tax: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryTobinTaxesRequest(betterproto.Message):
    """
    QueryTobinTaxesRequest is the request type for the Query/TobinTaxes RPC
    method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryTobinTaxesResponse(betterproto.Message):
    """
    QueryTobinTaxesResponse is response type for the Query/TobinTaxes RPC
    method.
    """

    # tobin_taxes defines a list of the tobin tax of all whitelisted denoms
    tobin_taxes: List["Denom"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryActivesRequest(betterproto.Message):
    """
    QueryActivesRequest is the request type for the Query/Actives RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryActivesResponse(betterproto.Message):
    """
    QueryActivesResponse is response type for the Query/Actives RPC method.
    """

    # actives defines a list of the denomination which oracle prices aggreed
    # upon.
    actives: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryVoteTargetsRequest(betterproto.Message):
    """
    QueryVoteTargetsRequest is the request type for the Query/VoteTargets RPC
    method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryVoteTargetsResponse(betterproto.Message):
    """
    QueryVoteTargetsResponse is response type for the Query/VoteTargets RPC
    method.
    """

    # vote_targets defines a list of the denomination in which everyone should
    # vote in the current vote period.
    vote_targets: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryFeederDelegationRequest(betterproto.Message):
    """
    QueryFeederDelegationRequest is the request type for the
    Query/FeederDelegation RPC method.
    """

    # validator defines the validator address to query for.
    validator_addr: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryFeederDelegationResponse(betterproto.Message):
    """
    QueryFeederDelegationResponse is response type for the
    Query/FeederDelegation RPC method.
    """

    # feeder_addr defines the feeder delegation of a validator
    feeder_addr: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryMissCounterRequest(betterproto.Message):
    """
    QueryMissCounterRequest is the request type for the Query/MissCounter RPC
    method.
    """

    # validator defines the validator address to query for.
    validator_addr: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryMissCounterResponse(betterproto.Message):
    """
    QueryMissCounterResponse is response type for the Query/MissCounter RPC
    method.
    """

    # miss_counter defines the oracle miss counter of a validator
    miss_counter: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class QueryAggregatePrevoteRequest(betterproto.Message):
    """
    QueryAggregatePrevoteRequest is the request type for the
    Query/AggregatePrevote RPC method.
    """

    # validator defines the validator address to query for.
    validator_addr: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryAggregatePrevoteResponse(betterproto.Message):
    """
    QueryAggregatePrevoteResponse is response type for the
    Query/AggregatePrevote RPC method.
    """

    # aggregate_prevote defines oracle aggregate prevote submitted by a validator
    # in the current vote period
    aggregate_prevote: "AggregateExchangeRatePrevote" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryAggregatePrevotesRequest(betterproto.Message):
    """
    QueryAggregatePrevotesRequest is the request type for the
    Query/AggregatePrevotes RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryAggregatePrevotesResponse(betterproto.Message):
    """
    QueryAggregatePrevotesResponse is response type for the
    Query/AggregatePrevotes RPC method.
    """

    # aggregate_prevotes defines all oracle aggregate prevotes submitted in the
    # current vote period
    aggregate_prevotes: List[
        "AggregateExchangeRatePrevote"
    ] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryAggregateVoteRequest(betterproto.Message):
    """
    QueryAggregateVoteRequest is the request type for the Query/AggregateVote
    RPC method.
    """

    # validator defines the validator address to query for.
    validator_addr: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryAggregateVoteResponse(betterproto.Message):
    """
    QueryAggregateVoteResponse is response type for the Query/AggregateVote RPC
    method.
    """

    # aggregate_vote defines oracle aggregate vote submitted by a validator in
    # the current vote period
    aggregate_vote: "AggregateExchangeRateVote" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryAggregateVotesRequest(betterproto.Message):
    """
    QueryAggregateVotesRequest is the request type for the Query/AggregateVotes
    RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryAggregateVotesResponse(betterproto.Message):
    """
    QueryAggregateVotesResponse is response type for the Query/AggregateVotes
    RPC method.
    """

    # aggregate_votes defines all oracle aggregate votes submitted in the current
    # vote period
    aggregate_votes: List["AggregateExchangeRateVote"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """
    QueryParamsRequest is the request type for the Query/Params RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse is the response type for the Query/Params RPC method.
    """

    # params defines the parameters of the module.
    params: "Params" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MsgAggregateExchangeRatePrevote(betterproto.Message):
    """
    MsgAggregateExchangeRatePrevote represents a message to submit aggregate
    exchange rate prevote.
    """

    hash: str = betterproto.string_field(1)
    feeder: str = betterproto.string_field(2)
    validator: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgAggregateExchangeRatePrevoteResponse(betterproto.Message):
    """
    MsgAggregateExchangeRatePrevoteResponse defines the
    Msg/AggregateExchangeRatePrevote response type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgAggregateExchangeRateVote(betterproto.Message):
    """
    MsgAggregateExchangeRateVote represents a message to submit aggregate
    exchange rate vote.
    """

    salt: str = betterproto.string_field(1)
    exchange_rates: str = betterproto.string_field(2)
    feeder: str = betterproto.string_field(3)
    validator: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class MsgAggregateExchangeRateVoteResponse(betterproto.Message):
    """
    MsgAggregateExchangeRateVoteResponse defines the
    Msg/AggregateExchangeRateVote response type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgDelegateFeedConsent(betterproto.Message):
    """
    MsgDelegateFeedConsent represents a message to delegate oracle voting
    rights to another address.
    """

    operator: str = betterproto.string_field(1)
    delegate: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class MsgDelegateFeedConsentResponse(betterproto.Message):
    """
    MsgDelegateFeedConsentResponse defines the Msg/DelegateFeedConsent response
    type.
    """

    pass


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the oracle module's genesis state."""

    params: "Params" = betterproto.message_field(1)
    feeder_delegations: List["FeederDelegation"] = betterproto.message_field(2)
    exchange_rates: List["ExchangeRateTuple"] = betterproto.message_field(3)
    miss_counters: List["MissCounter"] = betterproto.message_field(4)
    aggregate_exchange_rate_prevotes: List[
        "AggregateExchangeRatePrevote"
    ] = betterproto.message_field(5)
    aggregate_exchange_rate_votes: List[
        "AggregateExchangeRateVote"
    ] = betterproto.message_field(6)
    tobin_taxes: List["TobinTax"] = betterproto.message_field(7)


@dataclass(eq=False, repr=False)
class FeederDelegation(betterproto.Message):
    """
    FeederDelegation is the address for where oracle feeder authority are
    delegated to. By default this struct is only used at genesis to feed in
    default feeder addresses.
    """

    feeder_address: str = betterproto.string_field(1)
    validator_address: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class MissCounter(betterproto.Message):
    """
    MissCounter defines an miss counter and validator address pair used in
    oracle module's genesis state
    """

    validator_address: str = betterproto.string_field(1)
    miss_counter: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class TobinTax(betterproto.Message):
    """
    TobinTax defines an denom and tobin_tax pair used in oracle module's
    genesis state
    """

    denom: str = betterproto.string_field(1)
    tobin_tax: str = betterproto.string_field(2)


class QueryStub(betterproto.ServiceStub):
    async def exchange_rate(self, *, denom: str = "") -> "QueryExchangeRateResponse":

        request = QueryExchangeRateRequest()
        request.denom = denom

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/ExchangeRate",
            request,
            QueryExchangeRateResponse,
        )

    async def exchange_rates(self) -> "QueryExchangeRatesResponse":

        request = QueryExchangeRatesRequest()

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/ExchangeRates",
            request,
            QueryExchangeRatesResponse,
        )

    async def tobin_tax(self, *, denom: str = "") -> "QueryTobinTaxResponse":

        request = QueryTobinTaxRequest()
        request.denom = denom

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/TobinTax", request, QueryTobinTaxResponse
        )

    async def tobin_taxes(self) -> "QueryTobinTaxesResponse":

        request = QueryTobinTaxesRequest()

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/TobinTaxes", request, QueryTobinTaxesResponse
        )

    async def actives(self) -> "QueryActivesResponse":

        request = QueryActivesRequest()

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/Actives", request, QueryActivesResponse
        )

    async def vote_targets(self) -> "QueryVoteTargetsResponse":

        request = QueryVoteTargetsRequest()

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/VoteTargets", request, QueryVoteTargetsResponse
        )

    async def feeder_delegation(
        self, *, validator_addr: str = ""
    ) -> "QueryFeederDelegationResponse":

        request = QueryFeederDelegationRequest()
        request.validator_addr = validator_addr

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/FeederDelegation",
            request,
            QueryFeederDelegationResponse,
        )

    async def miss_counter(
        self, *, validator_addr: str = ""
    ) -> "QueryMissCounterResponse":

        request = QueryMissCounterRequest()
        request.validator_addr = validator_addr

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/MissCounter", request, QueryMissCounterResponse
        )

    async def aggregate_prevote(
        self, *, validator_addr: str = ""
    ) -> "QueryAggregatePrevoteResponse":

        request = QueryAggregatePrevoteRequest()
        request.validator_addr = validator_addr

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/AggregatePrevote",
            request,
            QueryAggregatePrevoteResponse,
        )

    async def aggregate_prevotes(self) -> "QueryAggregatePrevotesResponse":

        request = QueryAggregatePrevotesRequest()

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/AggregatePrevotes",
            request,
            QueryAggregatePrevotesResponse,
        )

    async def aggregate_vote(
        self, *, validator_addr: str = ""
    ) -> "QueryAggregateVoteResponse":

        request = QueryAggregateVoteRequest()
        request.validator_addr = validator_addr

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/AggregateVote",
            request,
            QueryAggregateVoteResponse,
        )

    async def aggregate_votes(self) -> "QueryAggregateVotesResponse":

        request = QueryAggregateVotesRequest()

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/AggregateVotes",
            request,
            QueryAggregateVotesResponse,
        )

    async def params(self) -> "QueryParamsResponse":

        request = QueryParamsRequest()

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Query/Params", request, QueryParamsResponse
        )


class MsgStub(betterproto.ServiceStub):
    async def aggregate_exchange_rate_prevote(
        self, *, hash: str = "", feeder: str = "", validator: str = ""
    ) -> "MsgAggregateExchangeRatePrevoteResponse":

        request = MsgAggregateExchangeRatePrevote()
        request.hash = hash
        request.feeder = feeder
        request.validator = validator

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Msg/AggregateExchangeRatePrevote",
            request,
            MsgAggregateExchangeRatePrevoteResponse,
        )

    async def aggregate_exchange_rate_vote(
        self,
        *,
        salt: str = "",
        exchange_rates: str = "",
        feeder: str = "",
        validator: str = "",
    ) -> "MsgAggregateExchangeRateVoteResponse":

        request = MsgAggregateExchangeRateVote()
        request.salt = salt
        request.exchange_rates = exchange_rates
        request.feeder = feeder
        request.validator = validator

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Msg/AggregateExchangeRateVote",
            request,
            MsgAggregateExchangeRateVoteResponse,
        )

    async def delegate_feed_consent(
        self, *, operator: str = "", delegate: str = ""
    ) -> "MsgDelegateFeedConsentResponse":

        request = MsgDelegateFeedConsent()
        request.operator = operator
        request.delegate = delegate

        return await self._unary_unary(
            "/terra.oracle.v1beta1.Msg/DelegateFeedConsent",
            request,
            MsgDelegateFeedConsentResponse,
        )


class QueryBase(ServiceBase):
    async def exchange_rate(self, denom: str) -> "QueryExchangeRateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def exchange_rates(self) -> "QueryExchangeRatesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def tobin_tax(self, denom: str) -> "QueryTobinTaxResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def tobin_taxes(self) -> "QueryTobinTaxesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def actives(self) -> "QueryActivesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def vote_targets(self) -> "QueryVoteTargetsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def feeder_delegation(
        self, validator_addr: str
    ) -> "QueryFeederDelegationResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def miss_counter(self, validator_addr: str) -> "QueryMissCounterResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def aggregate_prevote(
        self, validator_addr: str
    ) -> "QueryAggregatePrevoteResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def aggregate_prevotes(self) -> "QueryAggregatePrevotesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def aggregate_vote(self, validator_addr: str) -> "QueryAggregateVoteResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def aggregate_votes(self) -> "QueryAggregateVotesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(self) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_exchange_rate(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "denom": request.denom,
        }

        response = await self.exchange_rate(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_exchange_rates(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.exchange_rates(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_tobin_tax(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "denom": request.denom,
        }

        response = await self.tobin_tax(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_tobin_taxes(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.tobin_taxes(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_actives(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.actives(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_vote_targets(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.vote_targets(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_feeder_delegation(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "validator_addr": request.validator_addr,
        }

        response = await self.feeder_delegation(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_miss_counter(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "validator_addr": request.validator_addr,
        }

        response = await self.miss_counter(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_aggregate_prevote(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "validator_addr": request.validator_addr,
        }

        response = await self.aggregate_prevote(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_aggregate_prevotes(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.aggregate_prevotes(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_aggregate_vote(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "validator_addr": request.validator_addr,
        }

        response = await self.aggregate_vote(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_aggregate_votes(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.aggregate_votes(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_params(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.params(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/terra.oracle.v1beta1.Query/ExchangeRate": grpclib.const.Handler(
                self.__rpc_exchange_rate,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryExchangeRateRequest,
                QueryExchangeRateResponse,
            ),
            "/terra.oracle.v1beta1.Query/ExchangeRates": grpclib.const.Handler(
                self.__rpc_exchange_rates,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryExchangeRatesRequest,
                QueryExchangeRatesResponse,
            ),
            "/terra.oracle.v1beta1.Query/TobinTax": grpclib.const.Handler(
                self.__rpc_tobin_tax,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryTobinTaxRequest,
                QueryTobinTaxResponse,
            ),
            "/terra.oracle.v1beta1.Query/TobinTaxes": grpclib.const.Handler(
                self.__rpc_tobin_taxes,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryTobinTaxesRequest,
                QueryTobinTaxesResponse,
            ),
            "/terra.oracle.v1beta1.Query/Actives": grpclib.const.Handler(
                self.__rpc_actives,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryActivesRequest,
                QueryActivesResponse,
            ),
            "/terra.oracle.v1beta1.Query/VoteTargets": grpclib.const.Handler(
                self.__rpc_vote_targets,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryVoteTargetsRequest,
                QueryVoteTargetsResponse,
            ),
            "/terra.oracle.v1beta1.Query/FeederDelegation": grpclib.const.Handler(
                self.__rpc_feeder_delegation,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryFeederDelegationRequest,
                QueryFeederDelegationResponse,
            ),
            "/terra.oracle.v1beta1.Query/MissCounter": grpclib.const.Handler(
                self.__rpc_miss_counter,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryMissCounterRequest,
                QueryMissCounterResponse,
            ),
            "/terra.oracle.v1beta1.Query/AggregatePrevote": grpclib.const.Handler(
                self.__rpc_aggregate_prevote,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAggregatePrevoteRequest,
                QueryAggregatePrevoteResponse,
            ),
            "/terra.oracle.v1beta1.Query/AggregatePrevotes": grpclib.const.Handler(
                self.__rpc_aggregate_prevotes,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAggregatePrevotesRequest,
                QueryAggregatePrevotesResponse,
            ),
            "/terra.oracle.v1beta1.Query/AggregateVote": grpclib.const.Handler(
                self.__rpc_aggregate_vote,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAggregateVoteRequest,
                QueryAggregateVoteResponse,
            ),
            "/terra.oracle.v1beta1.Query/AggregateVotes": grpclib.const.Handler(
                self.__rpc_aggregate_votes,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAggregateVotesRequest,
                QueryAggregateVotesResponse,
            ),
            "/terra.oracle.v1beta1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def aggregate_exchange_rate_prevote(
        self, hash: str, feeder: str, validator: str
    ) -> "MsgAggregateExchangeRatePrevoteResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def aggregate_exchange_rate_vote(
        self, salt: str, exchange_rates: str, feeder: str, validator: str
    ) -> "MsgAggregateExchangeRateVoteResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def delegate_feed_consent(
        self, operator: str, delegate: str
    ) -> "MsgDelegateFeedConsentResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_aggregate_exchange_rate_prevote(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "hash": request.hash,
            "feeder": request.feeder,
            "validator": request.validator,
        }

        response = await self.aggregate_exchange_rate_prevote(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_aggregate_exchange_rate_vote(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "salt": request.salt,
            "exchange_rates": request.exchange_rates,
            "feeder": request.feeder,
            "validator": request.validator,
        }

        response = await self.aggregate_exchange_rate_vote(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_delegate_feed_consent(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "operator": request.operator,
            "delegate": request.delegate,
        }

        response = await self.delegate_feed_consent(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/terra.oracle.v1beta1.Msg/AggregateExchangeRatePrevote": grpclib.const.Handler(
                self.__rpc_aggregate_exchange_rate_prevote,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgAggregateExchangeRatePrevote,
                MsgAggregateExchangeRatePrevoteResponse,
            ),
            "/terra.oracle.v1beta1.Msg/AggregateExchangeRateVote": grpclib.const.Handler(
                self.__rpc_aggregate_exchange_rate_vote,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgAggregateExchangeRateVote,
                MsgAggregateExchangeRateVoteResponse,
            ),
            "/terra.oracle.v1beta1.Msg/DelegateFeedConsent": grpclib.const.Handler(
                self.__rpc_delegate_feed_consent,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgDelegateFeedConsent,
                MsgDelegateFeedConsentResponse,
            ),
        }


from ....cosmos.base import v1beta1 as ___cosmos_base_v1_beta1__
