//Generated by the protocol buffer compiler. DO NOT EDIT!
// source: ibc/core/channel/v1/tx.proto

package ibc.core.channel.v1;

@kotlin.jvm.JvmSynthetic
inline fun msgChannelOpenTryResponse(block: ibc.core.channel.v1.MsgChannelOpenTryResponseKt.Dsl.() -> Unit): ibc.core.channel.v1.Tx.MsgChannelOpenTryResponse =
  ibc.core.channel.v1.MsgChannelOpenTryResponseKt.Dsl._create(ibc.core.channel.v1.Tx.MsgChannelOpenTryResponse.newBuilder()).apply { block() }._build()
object MsgChannelOpenTryResponseKt {
  @kotlin.OptIn(com.google.protobuf.kotlin.OnlyForUseByGeneratedProtoCode::class)
  @com.google.protobuf.kotlin.ProtoDslMarker
  class Dsl private constructor(
    @kotlin.jvm.JvmField private val _builder: ibc.core.channel.v1.Tx.MsgChannelOpenTryResponse.Builder
  ) {
    companion object {
      @kotlin.jvm.JvmSynthetic
      @kotlin.PublishedApi
      internal fun _create(builder: ibc.core.channel.v1.Tx.MsgChannelOpenTryResponse.Builder): Dsl = Dsl(builder)
    }

    @kotlin.jvm.JvmSynthetic
    @kotlin.PublishedApi
    internal fun _build(): ibc.core.channel.v1.Tx.MsgChannelOpenTryResponse = _builder.build()
  }
}
@kotlin.jvm.JvmSynthetic
inline fun ibc.core.channel.v1.Tx.MsgChannelOpenTryResponse.copy(block: ibc.core.channel.v1.MsgChannelOpenTryResponseKt.Dsl.() -> Unit): ibc.core.channel.v1.Tx.MsgChannelOpenTryResponse =
  ibc.core.channel.v1.MsgChannelOpenTryResponseKt.Dsl._create(this.toBuilder()).apply { block() }._build()