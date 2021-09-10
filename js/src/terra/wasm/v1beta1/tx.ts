/* eslint-disable */
import Long from "long";
import {
  makeGenericClientConstructor,
  ChannelCredentials,
  ChannelOptions,
  UntypedServiceImplementation,
  handleUnaryCall,
  Client,
  ClientUnaryCall,
  Metadata,
  CallOptions,
  ServiceError,
} from "@grpc/grpc-js";
import _m0 from "protobufjs/minimal";
import { Coin } from "../../../cosmos/base/v1beta1/coin";

export const protobufPackage = "terra.wasm.v1beta1";

/**
 * MsgStoreCode represents a message to submit
 * Wasm code to the system
 */
export interface MsgStoreCode {
  /** Sender is the that actor that signed the messages */
  sender: string;
  /** WASMByteCode can be raw or gzip compressed */
  wasmByteCode: Uint8Array;
}

/** MsgStoreCodeResponse defines the Msg/StoreCode response type. */
export interface MsgStoreCodeResponse {
  /** CodeID is the reference to the stored WASM code */
  codeId: Long;
}

/**
 * MsgMigrateCode represents a message to submit
 * Wasm code to the system
 */
export interface MsgMigrateCode {
  /** CodeID is the migration target code id */
  codeId: Long;
  /** Sender is the that actor that signed the messages */
  sender: string;
  /** WASMByteCode can be raw or gzip compressed */
  wasmByteCode: Uint8Array;
}

/** MsgMigrateCodeResponse defines the Msg/MigrateCode response type. */
export interface MsgMigrateCodeResponse {}

/**
 * MsgInstantiateContract represents a message to create
 * a new smart contract instance for the given
 * code id.
 */
export interface MsgInstantiateContract {
  /** Sender is an sender address */
  sender: string;
  /** Admin is an optional admin address who can migrate the contract */
  admin: string;
  /** CodeID is the reference to the stored WASM code */
  codeId: Long;
  /** InitMsg json encoded message to be passed to the contract on instantiation */
  initMsg: Uint8Array;
  /** InitCoins that are transferred to the contract on execution */
  initCoins: Coin[];
}

/** MsgInstantiateContractResponse defines the Msg/InstantiateContract response type. */
export interface MsgInstantiateContractResponse {
  /** ContractAddress is the bech32 address of the new contract instance. */
  contractAddress: string;
  /** Data contains base64-encoded bytes to returned from the contract */
  data: Uint8Array;
}

/**
 * MsgExecuteContract represents a message to
 * submits the given message data to a smart contract.
 */
export interface MsgExecuteContract {
  /** Sender is the that actor that signed the messages */
  sender: string;
  /** Contract is the address of the smart contract */
  contract: string;
  /** ExecuteMsg json encoded message to be passed to the contract */
  executeMsg: Uint8Array;
  /** Coins that are transferred to the contract on execution */
  coins: Coin[];
}

/** MsgExecuteContractResponse defines the Msg/ExecuteContract response type. */
export interface MsgExecuteContractResponse {
  /** Data contains base64-encoded bytes to returned from the contract */
  data: Uint8Array;
}

/**
 * MsgMigrateContract represents a message to
 * runs a code upgrade/ downgrade for a smart contract
 */
export interface MsgMigrateContract {
  /** Admin is the current contract admin */
  admin: string;
  /** Contract is the address of the smart contract */
  contract: string;
  /** NewCodeID references the new WASM code */
  newCodeId: Long;
  /** MigrateMsg is json encoded message to be passed to the contract on migration */
  migrateMsg: Uint8Array;
}

/** MsgMigrateContractResponse defines the Msg/MigrateContract response type. */
export interface MsgMigrateContractResponse {
  /** Data contains base64-encoded bytes to returned from the contract */
  data: Uint8Array;
}

/**
 * MsgUpdateContractAdmin represents a message to
 * sets a new admin for a smart contract
 */
export interface MsgUpdateContractAdmin {
  /** Admin is the current contract admin */
  admin: string;
  /** NewAdmin is the new contract admin */
  newAdmin: string;
  /** Contract is the address of the smart contract */
  contract: string;
}

/** MsgUpdateContractAdminResponse defines the Msg/UpdateContractAdmin response type. */
export interface MsgUpdateContractAdminResponse {}

/**
 * MsgClearContractAdmin represents a message to
 * clear admin address from a smart contract
 */
export interface MsgClearContractAdmin {
  /** Admin is the current contract admin */
  admin: string;
  /** Contract is the address of the smart contract */
  contract: string;
}

/** MsgClearContractAdminResponse defines the Msg/ClearContractAdmin response type. */
export interface MsgClearContractAdminResponse {}

const baseMsgStoreCode: object = { sender: "" };

export const MsgStoreCode = {
  encode(message: MsgStoreCode, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.sender !== "") {
      writer.uint32(10).string(message.sender);
    }
    if (message.wasmByteCode.length !== 0) {
      writer.uint32(18).bytes(message.wasmByteCode);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgStoreCode {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgStoreCode } as MsgStoreCode;
    message.wasmByteCode = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.sender = reader.string();
          break;
        case 2:
          message.wasmByteCode = reader.bytes();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): MsgStoreCode {
    const message = { ...baseMsgStoreCode } as MsgStoreCode;
    message.wasmByteCode = new Uint8Array();
    if (object.sender !== undefined && object.sender !== null) {
      message.sender = String(object.sender);
    } else {
      message.sender = "";
    }
    if (object.wasmByteCode !== undefined && object.wasmByteCode !== null) {
      message.wasmByteCode = bytesFromBase64(object.wasmByteCode);
    }
    return message;
  },

  toJSON(message: MsgStoreCode): unknown {
    const obj: any = {};
    message.sender !== undefined && (obj.sender = message.sender);
    message.wasmByteCode !== undefined &&
      (obj.wasmByteCode = base64FromBytes(
        message.wasmByteCode !== undefined ? message.wasmByteCode : new Uint8Array(),
      ));
    return obj;
  },

  fromPartial(object: DeepPartial<MsgStoreCode>): MsgStoreCode {
    const message = { ...baseMsgStoreCode } as MsgStoreCode;
    if (object.sender !== undefined && object.sender !== null) {
      message.sender = object.sender;
    } else {
      message.sender = "";
    }
    if (object.wasmByteCode !== undefined && object.wasmByteCode !== null) {
      message.wasmByteCode = object.wasmByteCode;
    } else {
      message.wasmByteCode = new Uint8Array();
    }
    return message;
  },
};

const baseMsgStoreCodeResponse: object = { codeId: Long.UZERO };

export const MsgStoreCodeResponse = {
  encode(message: MsgStoreCodeResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (!message.codeId.isZero()) {
      writer.uint32(8).uint64(message.codeId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgStoreCodeResponse {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgStoreCodeResponse } as MsgStoreCodeResponse;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.codeId = reader.uint64() as Long;
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): MsgStoreCodeResponse {
    const message = { ...baseMsgStoreCodeResponse } as MsgStoreCodeResponse;
    if (object.codeId !== undefined && object.codeId !== null) {
      message.codeId = Long.fromString(object.codeId);
    } else {
      message.codeId = Long.UZERO;
    }
    return message;
  },

  toJSON(message: MsgStoreCodeResponse): unknown {
    const obj: any = {};
    message.codeId !== undefined && (obj.codeId = (message.codeId || Long.UZERO).toString());
    return obj;
  },

  fromPartial(object: DeepPartial<MsgStoreCodeResponse>): MsgStoreCodeResponse {
    const message = { ...baseMsgStoreCodeResponse } as MsgStoreCodeResponse;
    if (object.codeId !== undefined && object.codeId !== null) {
      message.codeId = object.codeId as Long;
    } else {
      message.codeId = Long.UZERO;
    }
    return message;
  },
};

const baseMsgMigrateCode: object = { codeId: Long.UZERO, sender: "" };

export const MsgMigrateCode = {
  encode(message: MsgMigrateCode, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (!message.codeId.isZero()) {
      writer.uint32(8).uint64(message.codeId);
    }
    if (message.sender !== "") {
      writer.uint32(18).string(message.sender);
    }
    if (message.wasmByteCode.length !== 0) {
      writer.uint32(26).bytes(message.wasmByteCode);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgMigrateCode {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgMigrateCode } as MsgMigrateCode;
    message.wasmByteCode = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.codeId = reader.uint64() as Long;
          break;
        case 2:
          message.sender = reader.string();
          break;
        case 3:
          message.wasmByteCode = reader.bytes();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): MsgMigrateCode {
    const message = { ...baseMsgMigrateCode } as MsgMigrateCode;
    message.wasmByteCode = new Uint8Array();
    if (object.codeId !== undefined && object.codeId !== null) {
      message.codeId = Long.fromString(object.codeId);
    } else {
      message.codeId = Long.UZERO;
    }
    if (object.sender !== undefined && object.sender !== null) {
      message.sender = String(object.sender);
    } else {
      message.sender = "";
    }
    if (object.wasmByteCode !== undefined && object.wasmByteCode !== null) {
      message.wasmByteCode = bytesFromBase64(object.wasmByteCode);
    }
    return message;
  },

  toJSON(message: MsgMigrateCode): unknown {
    const obj: any = {};
    message.codeId !== undefined && (obj.codeId = (message.codeId || Long.UZERO).toString());
    message.sender !== undefined && (obj.sender = message.sender);
    message.wasmByteCode !== undefined &&
      (obj.wasmByteCode = base64FromBytes(
        message.wasmByteCode !== undefined ? message.wasmByteCode : new Uint8Array(),
      ));
    return obj;
  },

  fromPartial(object: DeepPartial<MsgMigrateCode>): MsgMigrateCode {
    const message = { ...baseMsgMigrateCode } as MsgMigrateCode;
    if (object.codeId !== undefined && object.codeId !== null) {
      message.codeId = object.codeId as Long;
    } else {
      message.codeId = Long.UZERO;
    }
    if (object.sender !== undefined && object.sender !== null) {
      message.sender = object.sender;
    } else {
      message.sender = "";
    }
    if (object.wasmByteCode !== undefined && object.wasmByteCode !== null) {
      message.wasmByteCode = object.wasmByteCode;
    } else {
      message.wasmByteCode = new Uint8Array();
    }
    return message;
  },
};

const baseMsgMigrateCodeResponse: object = {};

export const MsgMigrateCodeResponse = {
  encode(_: MsgMigrateCodeResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgMigrateCodeResponse {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgMigrateCodeResponse } as MsgMigrateCodeResponse;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(_: any): MsgMigrateCodeResponse {
    const message = { ...baseMsgMigrateCodeResponse } as MsgMigrateCodeResponse;
    return message;
  },

  toJSON(_: MsgMigrateCodeResponse): unknown {
    const obj: any = {};
    return obj;
  },

  fromPartial(_: DeepPartial<MsgMigrateCodeResponse>): MsgMigrateCodeResponse {
    const message = { ...baseMsgMigrateCodeResponse } as MsgMigrateCodeResponse;
    return message;
  },
};

const baseMsgInstantiateContract: object = { sender: "", admin: "", codeId: Long.UZERO };

export const MsgInstantiateContract = {
  encode(message: MsgInstantiateContract, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.sender !== "") {
      writer.uint32(10).string(message.sender);
    }
    if (message.admin !== "") {
      writer.uint32(18).string(message.admin);
    }
    if (!message.codeId.isZero()) {
      writer.uint32(24).uint64(message.codeId);
    }
    if (message.initMsg.length !== 0) {
      writer.uint32(34).bytes(message.initMsg);
    }
    for (const v of message.initCoins) {
      Coin.encode(v!, writer.uint32(42).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgInstantiateContract {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgInstantiateContract } as MsgInstantiateContract;
    message.initCoins = [];
    message.initMsg = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.sender = reader.string();
          break;
        case 2:
          message.admin = reader.string();
          break;
        case 3:
          message.codeId = reader.uint64() as Long;
          break;
        case 4:
          message.initMsg = reader.bytes();
          break;
        case 5:
          message.initCoins.push(Coin.decode(reader, reader.uint32()));
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): MsgInstantiateContract {
    const message = { ...baseMsgInstantiateContract } as MsgInstantiateContract;
    message.initCoins = [];
    message.initMsg = new Uint8Array();
    if (object.sender !== undefined && object.sender !== null) {
      message.sender = String(object.sender);
    } else {
      message.sender = "";
    }
    if (object.admin !== undefined && object.admin !== null) {
      message.admin = String(object.admin);
    } else {
      message.admin = "";
    }
    if (object.codeId !== undefined && object.codeId !== null) {
      message.codeId = Long.fromString(object.codeId);
    } else {
      message.codeId = Long.UZERO;
    }
    if (object.initMsg !== undefined && object.initMsg !== null) {
      message.initMsg = bytesFromBase64(object.initMsg);
    }
    if (object.initCoins !== undefined && object.initCoins !== null) {
      for (const e of object.initCoins) {
        message.initCoins.push(Coin.fromJSON(e));
      }
    }
    return message;
  },

  toJSON(message: MsgInstantiateContract): unknown {
    const obj: any = {};
    message.sender !== undefined && (obj.sender = message.sender);
    message.admin !== undefined && (obj.admin = message.admin);
    message.codeId !== undefined && (obj.codeId = (message.codeId || Long.UZERO).toString());
    message.initMsg !== undefined &&
      (obj.initMsg = base64FromBytes(message.initMsg !== undefined ? message.initMsg : new Uint8Array()));
    if (message.initCoins) {
      obj.initCoins = message.initCoins.map((e) => (e ? Coin.toJSON(e) : undefined));
    } else {
      obj.initCoins = [];
    }
    return obj;
  },

  fromPartial(object: DeepPartial<MsgInstantiateContract>): MsgInstantiateContract {
    const message = { ...baseMsgInstantiateContract } as MsgInstantiateContract;
    message.initCoins = [];
    if (object.sender !== undefined && object.sender !== null) {
      message.sender = object.sender;
    } else {
      message.sender = "";
    }
    if (object.admin !== undefined && object.admin !== null) {
      message.admin = object.admin;
    } else {
      message.admin = "";
    }
    if (object.codeId !== undefined && object.codeId !== null) {
      message.codeId = object.codeId as Long;
    } else {
      message.codeId = Long.UZERO;
    }
    if (object.initMsg !== undefined && object.initMsg !== null) {
      message.initMsg = object.initMsg;
    } else {
      message.initMsg = new Uint8Array();
    }
    if (object.initCoins !== undefined && object.initCoins !== null) {
      for (const e of object.initCoins) {
        message.initCoins.push(Coin.fromPartial(e));
      }
    }
    return message;
  },
};

const baseMsgInstantiateContractResponse: object = { contractAddress: "" };

export const MsgInstantiateContractResponse = {
  encode(message: MsgInstantiateContractResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.contractAddress !== "") {
      writer.uint32(10).string(message.contractAddress);
    }
    if (message.data.length !== 0) {
      writer.uint32(18).bytes(message.data);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgInstantiateContractResponse {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgInstantiateContractResponse } as MsgInstantiateContractResponse;
    message.data = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.contractAddress = reader.string();
          break;
        case 2:
          message.data = reader.bytes();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): MsgInstantiateContractResponse {
    const message = { ...baseMsgInstantiateContractResponse } as MsgInstantiateContractResponse;
    message.data = new Uint8Array();
    if (object.contractAddress !== undefined && object.contractAddress !== null) {
      message.contractAddress = String(object.contractAddress);
    } else {
      message.contractAddress = "";
    }
    if (object.data !== undefined && object.data !== null) {
      message.data = bytesFromBase64(object.data);
    }
    return message;
  },

  toJSON(message: MsgInstantiateContractResponse): unknown {
    const obj: any = {};
    message.contractAddress !== undefined && (obj.contractAddress = message.contractAddress);
    message.data !== undefined &&
      (obj.data = base64FromBytes(message.data !== undefined ? message.data : new Uint8Array()));
    return obj;
  },

  fromPartial(object: DeepPartial<MsgInstantiateContractResponse>): MsgInstantiateContractResponse {
    const message = { ...baseMsgInstantiateContractResponse } as MsgInstantiateContractResponse;
    if (object.contractAddress !== undefined && object.contractAddress !== null) {
      message.contractAddress = object.contractAddress;
    } else {
      message.contractAddress = "";
    }
    if (object.data !== undefined && object.data !== null) {
      message.data = object.data;
    } else {
      message.data = new Uint8Array();
    }
    return message;
  },
};

const baseMsgExecuteContract: object = { sender: "", contract: "" };

export const MsgExecuteContract = {
  encode(message: MsgExecuteContract, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.sender !== "") {
      writer.uint32(10).string(message.sender);
    }
    if (message.contract !== "") {
      writer.uint32(18).string(message.contract);
    }
    if (message.executeMsg.length !== 0) {
      writer.uint32(26).bytes(message.executeMsg);
    }
    for (const v of message.coins) {
      Coin.encode(v!, writer.uint32(42).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgExecuteContract {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgExecuteContract } as MsgExecuteContract;
    message.coins = [];
    message.executeMsg = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.sender = reader.string();
          break;
        case 2:
          message.contract = reader.string();
          break;
        case 3:
          message.executeMsg = reader.bytes();
          break;
        case 5:
          message.coins.push(Coin.decode(reader, reader.uint32()));
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): MsgExecuteContract {
    const message = { ...baseMsgExecuteContract } as MsgExecuteContract;
    message.coins = [];
    message.executeMsg = new Uint8Array();
    if (object.sender !== undefined && object.sender !== null) {
      message.sender = String(object.sender);
    } else {
      message.sender = "";
    }
    if (object.contract !== undefined && object.contract !== null) {
      message.contract = String(object.contract);
    } else {
      message.contract = "";
    }
    if (object.executeMsg !== undefined && object.executeMsg !== null) {
      message.executeMsg = bytesFromBase64(object.executeMsg);
    }
    if (object.coins !== undefined && object.coins !== null) {
      for (const e of object.coins) {
        message.coins.push(Coin.fromJSON(e));
      }
    }
    return message;
  },

  toJSON(message: MsgExecuteContract): unknown {
    const obj: any = {};
    message.sender !== undefined && (obj.sender = message.sender);
    message.contract !== undefined && (obj.contract = message.contract);
    message.executeMsg !== undefined &&
      (obj.executeMsg = base64FromBytes(
        message.executeMsg !== undefined ? message.executeMsg : new Uint8Array(),
      ));
    if (message.coins) {
      obj.coins = message.coins.map((e) => (e ? Coin.toJSON(e) : undefined));
    } else {
      obj.coins = [];
    }
    return obj;
  },

  fromPartial(object: DeepPartial<MsgExecuteContract>): MsgExecuteContract {
    const message = { ...baseMsgExecuteContract } as MsgExecuteContract;
    message.coins = [];
    if (object.sender !== undefined && object.sender !== null) {
      message.sender = object.sender;
    } else {
      message.sender = "";
    }
    if (object.contract !== undefined && object.contract !== null) {
      message.contract = object.contract;
    } else {
      message.contract = "";
    }
    if (object.executeMsg !== undefined && object.executeMsg !== null) {
      message.executeMsg = object.executeMsg;
    } else {
      message.executeMsg = new Uint8Array();
    }
    if (object.coins !== undefined && object.coins !== null) {
      for (const e of object.coins) {
        message.coins.push(Coin.fromPartial(e));
      }
    }
    return message;
  },
};

const baseMsgExecuteContractResponse: object = {};

export const MsgExecuteContractResponse = {
  encode(message: MsgExecuteContractResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.data.length !== 0) {
      writer.uint32(10).bytes(message.data);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgExecuteContractResponse {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgExecuteContractResponse } as MsgExecuteContractResponse;
    message.data = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.data = reader.bytes();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): MsgExecuteContractResponse {
    const message = { ...baseMsgExecuteContractResponse } as MsgExecuteContractResponse;
    message.data = new Uint8Array();
    if (object.data !== undefined && object.data !== null) {
      message.data = bytesFromBase64(object.data);
    }
    return message;
  },

  toJSON(message: MsgExecuteContractResponse): unknown {
    const obj: any = {};
    message.data !== undefined &&
      (obj.data = base64FromBytes(message.data !== undefined ? message.data : new Uint8Array()));
    return obj;
  },

  fromPartial(object: DeepPartial<MsgExecuteContractResponse>): MsgExecuteContractResponse {
    const message = { ...baseMsgExecuteContractResponse } as MsgExecuteContractResponse;
    if (object.data !== undefined && object.data !== null) {
      message.data = object.data;
    } else {
      message.data = new Uint8Array();
    }
    return message;
  },
};

const baseMsgMigrateContract: object = { admin: "", contract: "", newCodeId: Long.UZERO };

export const MsgMigrateContract = {
  encode(message: MsgMigrateContract, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.admin !== "") {
      writer.uint32(10).string(message.admin);
    }
    if (message.contract !== "") {
      writer.uint32(18).string(message.contract);
    }
    if (!message.newCodeId.isZero()) {
      writer.uint32(24).uint64(message.newCodeId);
    }
    if (message.migrateMsg.length !== 0) {
      writer.uint32(34).bytes(message.migrateMsg);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgMigrateContract {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgMigrateContract } as MsgMigrateContract;
    message.migrateMsg = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.admin = reader.string();
          break;
        case 2:
          message.contract = reader.string();
          break;
        case 3:
          message.newCodeId = reader.uint64() as Long;
          break;
        case 4:
          message.migrateMsg = reader.bytes();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): MsgMigrateContract {
    const message = { ...baseMsgMigrateContract } as MsgMigrateContract;
    message.migrateMsg = new Uint8Array();
    if (object.admin !== undefined && object.admin !== null) {
      message.admin = String(object.admin);
    } else {
      message.admin = "";
    }
    if (object.contract !== undefined && object.contract !== null) {
      message.contract = String(object.contract);
    } else {
      message.contract = "";
    }
    if (object.newCodeId !== undefined && object.newCodeId !== null) {
      message.newCodeId = Long.fromString(object.newCodeId);
    } else {
      message.newCodeId = Long.UZERO;
    }
    if (object.migrateMsg !== undefined && object.migrateMsg !== null) {
      message.migrateMsg = bytesFromBase64(object.migrateMsg);
    }
    return message;
  },

  toJSON(message: MsgMigrateContract): unknown {
    const obj: any = {};
    message.admin !== undefined && (obj.admin = message.admin);
    message.contract !== undefined && (obj.contract = message.contract);
    message.newCodeId !== undefined && (obj.newCodeId = (message.newCodeId || Long.UZERO).toString());
    message.migrateMsg !== undefined &&
      (obj.migrateMsg = base64FromBytes(
        message.migrateMsg !== undefined ? message.migrateMsg : new Uint8Array(),
      ));
    return obj;
  },

  fromPartial(object: DeepPartial<MsgMigrateContract>): MsgMigrateContract {
    const message = { ...baseMsgMigrateContract } as MsgMigrateContract;
    if (object.admin !== undefined && object.admin !== null) {
      message.admin = object.admin;
    } else {
      message.admin = "";
    }
    if (object.contract !== undefined && object.contract !== null) {
      message.contract = object.contract;
    } else {
      message.contract = "";
    }
    if (object.newCodeId !== undefined && object.newCodeId !== null) {
      message.newCodeId = object.newCodeId as Long;
    } else {
      message.newCodeId = Long.UZERO;
    }
    if (object.migrateMsg !== undefined && object.migrateMsg !== null) {
      message.migrateMsg = object.migrateMsg;
    } else {
      message.migrateMsg = new Uint8Array();
    }
    return message;
  },
};

const baseMsgMigrateContractResponse: object = {};

export const MsgMigrateContractResponse = {
  encode(message: MsgMigrateContractResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.data.length !== 0) {
      writer.uint32(10).bytes(message.data);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgMigrateContractResponse {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgMigrateContractResponse } as MsgMigrateContractResponse;
    message.data = new Uint8Array();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.data = reader.bytes();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): MsgMigrateContractResponse {
    const message = { ...baseMsgMigrateContractResponse } as MsgMigrateContractResponse;
    message.data = new Uint8Array();
    if (object.data !== undefined && object.data !== null) {
      message.data = bytesFromBase64(object.data);
    }
    return message;
  },

  toJSON(message: MsgMigrateContractResponse): unknown {
    const obj: any = {};
    message.data !== undefined &&
      (obj.data = base64FromBytes(message.data !== undefined ? message.data : new Uint8Array()));
    return obj;
  },

  fromPartial(object: DeepPartial<MsgMigrateContractResponse>): MsgMigrateContractResponse {
    const message = { ...baseMsgMigrateContractResponse } as MsgMigrateContractResponse;
    if (object.data !== undefined && object.data !== null) {
      message.data = object.data;
    } else {
      message.data = new Uint8Array();
    }
    return message;
  },
};

const baseMsgUpdateContractAdmin: object = { admin: "", newAdmin: "", contract: "" };

export const MsgUpdateContractAdmin = {
  encode(message: MsgUpdateContractAdmin, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.admin !== "") {
      writer.uint32(10).string(message.admin);
    }
    if (message.newAdmin !== "") {
      writer.uint32(18).string(message.newAdmin);
    }
    if (message.contract !== "") {
      writer.uint32(26).string(message.contract);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgUpdateContractAdmin {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgUpdateContractAdmin } as MsgUpdateContractAdmin;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.admin = reader.string();
          break;
        case 2:
          message.newAdmin = reader.string();
          break;
        case 3:
          message.contract = reader.string();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): MsgUpdateContractAdmin {
    const message = { ...baseMsgUpdateContractAdmin } as MsgUpdateContractAdmin;
    if (object.admin !== undefined && object.admin !== null) {
      message.admin = String(object.admin);
    } else {
      message.admin = "";
    }
    if (object.newAdmin !== undefined && object.newAdmin !== null) {
      message.newAdmin = String(object.newAdmin);
    } else {
      message.newAdmin = "";
    }
    if (object.contract !== undefined && object.contract !== null) {
      message.contract = String(object.contract);
    } else {
      message.contract = "";
    }
    return message;
  },

  toJSON(message: MsgUpdateContractAdmin): unknown {
    const obj: any = {};
    message.admin !== undefined && (obj.admin = message.admin);
    message.newAdmin !== undefined && (obj.newAdmin = message.newAdmin);
    message.contract !== undefined && (obj.contract = message.contract);
    return obj;
  },

  fromPartial(object: DeepPartial<MsgUpdateContractAdmin>): MsgUpdateContractAdmin {
    const message = { ...baseMsgUpdateContractAdmin } as MsgUpdateContractAdmin;
    if (object.admin !== undefined && object.admin !== null) {
      message.admin = object.admin;
    } else {
      message.admin = "";
    }
    if (object.newAdmin !== undefined && object.newAdmin !== null) {
      message.newAdmin = object.newAdmin;
    } else {
      message.newAdmin = "";
    }
    if (object.contract !== undefined && object.contract !== null) {
      message.contract = object.contract;
    } else {
      message.contract = "";
    }
    return message;
  },
};

const baseMsgUpdateContractAdminResponse: object = {};

export const MsgUpdateContractAdminResponse = {
  encode(_: MsgUpdateContractAdminResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgUpdateContractAdminResponse {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgUpdateContractAdminResponse } as MsgUpdateContractAdminResponse;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(_: any): MsgUpdateContractAdminResponse {
    const message = { ...baseMsgUpdateContractAdminResponse } as MsgUpdateContractAdminResponse;
    return message;
  },

  toJSON(_: MsgUpdateContractAdminResponse): unknown {
    const obj: any = {};
    return obj;
  },

  fromPartial(_: DeepPartial<MsgUpdateContractAdminResponse>): MsgUpdateContractAdminResponse {
    const message = { ...baseMsgUpdateContractAdminResponse } as MsgUpdateContractAdminResponse;
    return message;
  },
};

const baseMsgClearContractAdmin: object = { admin: "", contract: "" };

export const MsgClearContractAdmin = {
  encode(message: MsgClearContractAdmin, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.admin !== "") {
      writer.uint32(10).string(message.admin);
    }
    if (message.contract !== "") {
      writer.uint32(18).string(message.contract);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgClearContractAdmin {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgClearContractAdmin } as MsgClearContractAdmin;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.admin = reader.string();
          break;
        case 2:
          message.contract = reader.string();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): MsgClearContractAdmin {
    const message = { ...baseMsgClearContractAdmin } as MsgClearContractAdmin;
    if (object.admin !== undefined && object.admin !== null) {
      message.admin = String(object.admin);
    } else {
      message.admin = "";
    }
    if (object.contract !== undefined && object.contract !== null) {
      message.contract = String(object.contract);
    } else {
      message.contract = "";
    }
    return message;
  },

  toJSON(message: MsgClearContractAdmin): unknown {
    const obj: any = {};
    message.admin !== undefined && (obj.admin = message.admin);
    message.contract !== undefined && (obj.contract = message.contract);
    return obj;
  },

  fromPartial(object: DeepPartial<MsgClearContractAdmin>): MsgClearContractAdmin {
    const message = { ...baseMsgClearContractAdmin } as MsgClearContractAdmin;
    if (object.admin !== undefined && object.admin !== null) {
      message.admin = object.admin;
    } else {
      message.admin = "";
    }
    if (object.contract !== undefined && object.contract !== null) {
      message.contract = object.contract;
    } else {
      message.contract = "";
    }
    return message;
  },
};

const baseMsgClearContractAdminResponse: object = {};

export const MsgClearContractAdminResponse = {
  encode(_: MsgClearContractAdminResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): MsgClearContractAdminResponse {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseMsgClearContractAdminResponse } as MsgClearContractAdminResponse;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(_: any): MsgClearContractAdminResponse {
    const message = { ...baseMsgClearContractAdminResponse } as MsgClearContractAdminResponse;
    return message;
  },

  toJSON(_: MsgClearContractAdminResponse): unknown {
    const obj: any = {};
    return obj;
  },

  fromPartial(_: DeepPartial<MsgClearContractAdminResponse>): MsgClearContractAdminResponse {
    const message = { ...baseMsgClearContractAdminResponse } as MsgClearContractAdminResponse;
    return message;
  },
};

/** Msg defines the oracle Msg service. */
export const MsgService = {
  /** StoreCode to submit Wasm code to the system */
  storeCode: {
    path: "/terra.wasm.v1beta1.Msg/StoreCode",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: MsgStoreCode) => Buffer.from(MsgStoreCode.encode(value).finish()),
    requestDeserialize: (value: Buffer) => MsgStoreCode.decode(value),
    responseSerialize: (value: MsgStoreCodeResponse) =>
      Buffer.from(MsgStoreCodeResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => MsgStoreCodeResponse.decode(value),
  },
  /** MigrateCode to submit new version Wasm code to the system */
  migrateCode: {
    path: "/terra.wasm.v1beta1.Msg/MigrateCode",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: MsgMigrateCode) => Buffer.from(MsgMigrateCode.encode(value).finish()),
    requestDeserialize: (value: Buffer) => MsgMigrateCode.decode(value),
    responseSerialize: (value: MsgMigrateCodeResponse) =>
      Buffer.from(MsgMigrateCodeResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => MsgMigrateCodeResponse.decode(value),
  },
  /** Instantiate creates a new smart contract instance for the given code id. */
  instantiateContract: {
    path: "/terra.wasm.v1beta1.Msg/InstantiateContract",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: MsgInstantiateContract) =>
      Buffer.from(MsgInstantiateContract.encode(value).finish()),
    requestDeserialize: (value: Buffer) => MsgInstantiateContract.decode(value),
    responseSerialize: (value: MsgInstantiateContractResponse) =>
      Buffer.from(MsgInstantiateContractResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => MsgInstantiateContractResponse.decode(value),
  },
  /** Execute submits the given message data to a smart contract */
  executeContract: {
    path: "/terra.wasm.v1beta1.Msg/ExecuteContract",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: MsgExecuteContract) => Buffer.from(MsgExecuteContract.encode(value).finish()),
    requestDeserialize: (value: Buffer) => MsgExecuteContract.decode(value),
    responseSerialize: (value: MsgExecuteContractResponse) =>
      Buffer.from(MsgExecuteContractResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => MsgExecuteContractResponse.decode(value),
  },
  /** Migrate runs a code upgrade/ downgrade for a smart contract */
  migrateContract: {
    path: "/terra.wasm.v1beta1.Msg/MigrateContract",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: MsgMigrateContract) => Buffer.from(MsgMigrateContract.encode(value).finish()),
    requestDeserialize: (value: Buffer) => MsgMigrateContract.decode(value),
    responseSerialize: (value: MsgMigrateContractResponse) =>
      Buffer.from(MsgMigrateContractResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => MsgMigrateContractResponse.decode(value),
  },
  /** UpdateContractAdmin sets a new admin for a smart contract */
  updateContractAdmin: {
    path: "/terra.wasm.v1beta1.Msg/UpdateContractAdmin",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: MsgUpdateContractAdmin) =>
      Buffer.from(MsgUpdateContractAdmin.encode(value).finish()),
    requestDeserialize: (value: Buffer) => MsgUpdateContractAdmin.decode(value),
    responseSerialize: (value: MsgUpdateContractAdminResponse) =>
      Buffer.from(MsgUpdateContractAdminResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => MsgUpdateContractAdminResponse.decode(value),
  },
  /** ClearContractAdmin remove admin flag from a smart contract */
  clearContractAdmin: {
    path: "/terra.wasm.v1beta1.Msg/ClearContractAdmin",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: MsgClearContractAdmin) =>
      Buffer.from(MsgClearContractAdmin.encode(value).finish()),
    requestDeserialize: (value: Buffer) => MsgClearContractAdmin.decode(value),
    responseSerialize: (value: MsgClearContractAdminResponse) =>
      Buffer.from(MsgClearContractAdminResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => MsgClearContractAdminResponse.decode(value),
  },
} as const;

export interface MsgServer extends UntypedServiceImplementation {
  /** StoreCode to submit Wasm code to the system */
  storeCode: handleUnaryCall<MsgStoreCode, MsgStoreCodeResponse>;
  /** MigrateCode to submit new version Wasm code to the system */
  migrateCode: handleUnaryCall<MsgMigrateCode, MsgMigrateCodeResponse>;
  /** Instantiate creates a new smart contract instance for the given code id. */
  instantiateContract: handleUnaryCall<MsgInstantiateContract, MsgInstantiateContractResponse>;
  /** Execute submits the given message data to a smart contract */
  executeContract: handleUnaryCall<MsgExecuteContract, MsgExecuteContractResponse>;
  /** Migrate runs a code upgrade/ downgrade for a smart contract */
  migrateContract: handleUnaryCall<MsgMigrateContract, MsgMigrateContractResponse>;
  /** UpdateContractAdmin sets a new admin for a smart contract */
  updateContractAdmin: handleUnaryCall<MsgUpdateContractAdmin, MsgUpdateContractAdminResponse>;
  /** ClearContractAdmin remove admin flag from a smart contract */
  clearContractAdmin: handleUnaryCall<MsgClearContractAdmin, MsgClearContractAdminResponse>;
}

export interface MsgClient extends Client {
  /** StoreCode to submit Wasm code to the system */
  storeCode(
    request: MsgStoreCode,
    callback: (error: ServiceError | null, response: MsgStoreCodeResponse) => void,
  ): ClientUnaryCall;
  storeCode(
    request: MsgStoreCode,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: MsgStoreCodeResponse) => void,
  ): ClientUnaryCall;
  storeCode(
    request: MsgStoreCode,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: MsgStoreCodeResponse) => void,
  ): ClientUnaryCall;
  /** MigrateCode to submit new version Wasm code to the system */
  migrateCode(
    request: MsgMigrateCode,
    callback: (error: ServiceError | null, response: MsgMigrateCodeResponse) => void,
  ): ClientUnaryCall;
  migrateCode(
    request: MsgMigrateCode,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: MsgMigrateCodeResponse) => void,
  ): ClientUnaryCall;
  migrateCode(
    request: MsgMigrateCode,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: MsgMigrateCodeResponse) => void,
  ): ClientUnaryCall;
  /** Instantiate creates a new smart contract instance for the given code id. */
  instantiateContract(
    request: MsgInstantiateContract,
    callback: (error: ServiceError | null, response: MsgInstantiateContractResponse) => void,
  ): ClientUnaryCall;
  instantiateContract(
    request: MsgInstantiateContract,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: MsgInstantiateContractResponse) => void,
  ): ClientUnaryCall;
  instantiateContract(
    request: MsgInstantiateContract,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: MsgInstantiateContractResponse) => void,
  ): ClientUnaryCall;
  /** Execute submits the given message data to a smart contract */
  executeContract(
    request: MsgExecuteContract,
    callback: (error: ServiceError | null, response: MsgExecuteContractResponse) => void,
  ): ClientUnaryCall;
  executeContract(
    request: MsgExecuteContract,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: MsgExecuteContractResponse) => void,
  ): ClientUnaryCall;
  executeContract(
    request: MsgExecuteContract,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: MsgExecuteContractResponse) => void,
  ): ClientUnaryCall;
  /** Migrate runs a code upgrade/ downgrade for a smart contract */
  migrateContract(
    request: MsgMigrateContract,
    callback: (error: ServiceError | null, response: MsgMigrateContractResponse) => void,
  ): ClientUnaryCall;
  migrateContract(
    request: MsgMigrateContract,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: MsgMigrateContractResponse) => void,
  ): ClientUnaryCall;
  migrateContract(
    request: MsgMigrateContract,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: MsgMigrateContractResponse) => void,
  ): ClientUnaryCall;
  /** UpdateContractAdmin sets a new admin for a smart contract */
  updateContractAdmin(
    request: MsgUpdateContractAdmin,
    callback: (error: ServiceError | null, response: MsgUpdateContractAdminResponse) => void,
  ): ClientUnaryCall;
  updateContractAdmin(
    request: MsgUpdateContractAdmin,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: MsgUpdateContractAdminResponse) => void,
  ): ClientUnaryCall;
  updateContractAdmin(
    request: MsgUpdateContractAdmin,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: MsgUpdateContractAdminResponse) => void,
  ): ClientUnaryCall;
  /** ClearContractAdmin remove admin flag from a smart contract */
  clearContractAdmin(
    request: MsgClearContractAdmin,
    callback: (error: ServiceError | null, response: MsgClearContractAdminResponse) => void,
  ): ClientUnaryCall;
  clearContractAdmin(
    request: MsgClearContractAdmin,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: MsgClearContractAdminResponse) => void,
  ): ClientUnaryCall;
  clearContractAdmin(
    request: MsgClearContractAdmin,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: MsgClearContractAdminResponse) => void,
  ): ClientUnaryCall;
}

export const MsgClient = makeGenericClientConstructor(MsgService, "terra.wasm.v1beta1.Msg") as unknown as {
  new (address: string, credentials: ChannelCredentials, options?: Partial<ChannelOptions>): MsgClient;
};

declare var self: any | undefined;
declare var window: any | undefined;
var globalThis: any = (() => {
  if (typeof globalThis !== "undefined") return globalThis;
  if (typeof self !== "undefined") return self;
  if (typeof window !== "undefined") return window;
  if (typeof global !== "undefined") return global;
  throw "Unable to locate global object";
})();

const atob: (b64: string) => string =
  globalThis.atob || ((b64) => globalThis.Buffer.from(b64, "base64").toString("binary"));
function bytesFromBase64(b64: string): Uint8Array {
  const bin = atob(b64);
  const arr = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; ++i) {
    arr[i] = bin.charCodeAt(i);
  }
  return arr;
}

const btoa: (bin: string) => string =
  globalThis.btoa || ((bin) => globalThis.Buffer.from(bin, "binary").toString("base64"));
function base64FromBytes(arr: Uint8Array): string {
  const bin: string[] = [];
  for (const byte of arr) {
    bin.push(String.fromCharCode(byte));
  }
  return btoa(bin.join(""));
}

type Builtin = Date | Function | Uint8Array | string | number | boolean | undefined | Long;
export type DeepPartial<T> = T extends Builtin
  ? T
  : T extends Array<infer U>
  ? Array<DeepPartial<U>>
  : T extends ReadonlyArray<infer U>
  ? ReadonlyArray<DeepPartial<U>>
  : T extends {}
  ? { [K in keyof T]?: DeepPartial<T[K]> }
  : Partial<T>;

if (_m0.util.Long !== Long) {
  _m0.util.Long = Long as any;
  _m0.configure();
}
