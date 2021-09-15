//Generated by the protocol buffer compiler. DO NOT EDIT!
// source: cosmos/base/abci/v1beta1/abci.proto

package cosmos.base.abci.v1beta1;

@kotlin.jvm.JvmSynthetic
inline fun simulationResponse(block: cosmos.base.abci.v1beta1.SimulationResponseKt.Dsl.() -> Unit): cosmos.base.abci.v1beta1.Abci.SimulationResponse =
  cosmos.base.abci.v1beta1.SimulationResponseKt.Dsl._create(cosmos.base.abci.v1beta1.Abci.SimulationResponse.newBuilder()).apply { block() }._build()
object SimulationResponseKt {
  @kotlin.OptIn(com.google.protobuf.kotlin.OnlyForUseByGeneratedProtoCode::class)
  @com.google.protobuf.kotlin.ProtoDslMarker
  class Dsl private constructor(
    @kotlin.jvm.JvmField private val _builder: cosmos.base.abci.v1beta1.Abci.SimulationResponse.Builder
  ) {
    companion object {
      @kotlin.jvm.JvmSynthetic
      @kotlin.PublishedApi
      internal fun _create(builder: cosmos.base.abci.v1beta1.Abci.SimulationResponse.Builder): Dsl = Dsl(builder)
    }

    @kotlin.jvm.JvmSynthetic
    @kotlin.PublishedApi
    internal fun _build(): cosmos.base.abci.v1beta1.Abci.SimulationResponse = _builder.build()

    /**
     * <code>.cosmos.base.abci.v1beta1.GasInfo gas_info = 1 [(.gogoproto.nullable) = false, (.gogoproto.embed) = true];</code>
     */
    var gasInfo: cosmos.base.abci.v1beta1.Abci.GasInfo
      @JvmName("getGasInfo")
      get() = _builder.getGasInfo()
      @JvmName("setGasInfo")
      set(value) {
        _builder.setGasInfo(value)
      }
    /**
     * <code>.cosmos.base.abci.v1beta1.GasInfo gas_info = 1 [(.gogoproto.nullable) = false, (.gogoproto.embed) = true];</code>
     */
    fun clearGasInfo() {
      _builder.clearGasInfo()
    }
    /**
     * <code>.cosmos.base.abci.v1beta1.GasInfo gas_info = 1 [(.gogoproto.nullable) = false, (.gogoproto.embed) = true];</code>
     * @return Whether the gasInfo field is set.
     */
    fun hasGasInfo(): kotlin.Boolean {
      return _builder.hasGasInfo()
    }

    /**
     * <code>.cosmos.base.abci.v1beta1.Result result = 2;</code>
     */
    var result: cosmos.base.abci.v1beta1.Abci.Result
      @JvmName("getResult")
      get() = _builder.getResult()
      @JvmName("setResult")
      set(value) {
        _builder.setResult(value)
      }
    /**
     * <code>.cosmos.base.abci.v1beta1.Result result = 2;</code>
     */
    fun clearResult() {
      _builder.clearResult()
    }
    /**
     * <code>.cosmos.base.abci.v1beta1.Result result = 2;</code>
     * @return Whether the result field is set.
     */
    fun hasResult(): kotlin.Boolean {
      return _builder.hasResult()
    }
  }
}
@kotlin.jvm.JvmSynthetic
inline fun cosmos.base.abci.v1beta1.Abci.SimulationResponse.copy(block: cosmos.base.abci.v1beta1.SimulationResponseKt.Dsl.() -> Unit): cosmos.base.abci.v1beta1.Abci.SimulationResponse =
  cosmos.base.abci.v1beta1.SimulationResponseKt.Dsl._create(this.toBuilder()).apply { block() }._build()