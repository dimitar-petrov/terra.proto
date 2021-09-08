// source: terra/market/v1beta1/market.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {missingRequire} reports error on implicit type usages.
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

var gogoproto_gogo_pb = require('../../../gogoproto/gogo_pb.js');
goog.object.extend(proto, gogoproto_gogo_pb);
goog.exportSymbol('proto.terra.market.v1beta1.Params', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.terra.market.v1beta1.Params = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.terra.market.v1beta1.Params, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.terra.market.v1beta1.Params.displayName = 'proto.terra.market.v1beta1.Params';
}



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.terra.market.v1beta1.Params.prototype.toObject = function(opt_includeInstance) {
  return proto.terra.market.v1beta1.Params.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.terra.market.v1beta1.Params} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.terra.market.v1beta1.Params.toObject = function(includeInstance, msg) {
  var f, obj = {
    basePool: msg.getBasePool_asB64(),
    poolRecoveryPeriod: jspb.Message.getFieldWithDefault(msg, 2, 0),
    minStabilitySpread: msg.getMinStabilitySpread_asB64()
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.terra.market.v1beta1.Params}
 */
proto.terra.market.v1beta1.Params.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.terra.market.v1beta1.Params;
  return proto.terra.market.v1beta1.Params.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.terra.market.v1beta1.Params} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.terra.market.v1beta1.Params}
 */
proto.terra.market.v1beta1.Params.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {!Uint8Array} */ (reader.readBytes());
      msg.setBasePool(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readUint64());
      msg.setPoolRecoveryPeriod(value);
      break;
    case 3:
      var value = /** @type {!Uint8Array} */ (reader.readBytes());
      msg.setMinStabilitySpread(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.terra.market.v1beta1.Params.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.terra.market.v1beta1.Params.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.terra.market.v1beta1.Params} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.terra.market.v1beta1.Params.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBasePool_asU8();
  if (f.length > 0) {
    writer.writeBytes(
      1,
      f
    );
  }
  f = message.getPoolRecoveryPeriod();
  if (f !== 0) {
    writer.writeUint64(
      2,
      f
    );
  }
  f = message.getMinStabilitySpread_asU8();
  if (f.length > 0) {
    writer.writeBytes(
      3,
      f
    );
  }
};


/**
 * optional bytes base_pool = 1;
 * @return {!(string|Uint8Array)}
 */
proto.terra.market.v1beta1.Params.prototype.getBasePool = function() {
  return /** @type {!(string|Uint8Array)} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * optional bytes base_pool = 1;
 * This is a type-conversion wrapper around `getBasePool()`
 * @return {string}
 */
proto.terra.market.v1beta1.Params.prototype.getBasePool_asB64 = function() {
  return /** @type {string} */ (jspb.Message.bytesAsB64(
      this.getBasePool()));
};


/**
 * optional bytes base_pool = 1;
 * Note that Uint8Array is not supported on all browsers.
 * @see http://caniuse.com/Uint8Array
 * This is a type-conversion wrapper around `getBasePool()`
 * @return {!Uint8Array}
 */
proto.terra.market.v1beta1.Params.prototype.getBasePool_asU8 = function() {
  return /** @type {!Uint8Array} */ (jspb.Message.bytesAsU8(
      this.getBasePool()));
};


/**
 * @param {!(string|Uint8Array)} value
 * @return {!proto.terra.market.v1beta1.Params} returns this
 */
proto.terra.market.v1beta1.Params.prototype.setBasePool = function(value) {
  return jspb.Message.setProto3BytesField(this, 1, value);
};


/**
 * optional uint64 pool_recovery_period = 2;
 * @return {number}
 */
proto.terra.market.v1beta1.Params.prototype.getPoolRecoveryPeriod = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/**
 * @param {number} value
 * @return {!proto.terra.market.v1beta1.Params} returns this
 */
proto.terra.market.v1beta1.Params.prototype.setPoolRecoveryPeriod = function(value) {
  return jspb.Message.setProto3IntField(this, 2, value);
};


/**
 * optional bytes min_stability_spread = 3;
 * @return {!(string|Uint8Array)}
 */
proto.terra.market.v1beta1.Params.prototype.getMinStabilitySpread = function() {
  return /** @type {!(string|Uint8Array)} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/**
 * optional bytes min_stability_spread = 3;
 * This is a type-conversion wrapper around `getMinStabilitySpread()`
 * @return {string}
 */
proto.terra.market.v1beta1.Params.prototype.getMinStabilitySpread_asB64 = function() {
  return /** @type {string} */ (jspb.Message.bytesAsB64(
      this.getMinStabilitySpread()));
};


/**
 * optional bytes min_stability_spread = 3;
 * Note that Uint8Array is not supported on all browsers.
 * @see http://caniuse.com/Uint8Array
 * This is a type-conversion wrapper around `getMinStabilitySpread()`
 * @return {!Uint8Array}
 */
proto.terra.market.v1beta1.Params.prototype.getMinStabilitySpread_asU8 = function() {
  return /** @type {!Uint8Array} */ (jspb.Message.bytesAsU8(
      this.getMinStabilitySpread()));
};


/**
 * @param {!(string|Uint8Array)} value
 * @return {!proto.terra.market.v1beta1.Params} returns this
 */
proto.terra.market.v1beta1.Params.prototype.setMinStabilitySpread = function(value) {
  return jspb.Message.setProto3BytesField(this, 3, value);
};


goog.object.extend(exports, proto.terra.market.v1beta1);