# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: raft.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'raft.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\"d\n\x0bVoteRequest\x12\x15\n\rcandidateTerm\x18\x01 \x01(\x04\x12\x13\n\x0b\x63\x61ndidateId\x18\x02 \x01(\x04\x12\x14\n\x0clastLogIndex\x18\x03 \x01(\x04\x12\x13\n\x0blastLogTerm\x18\x04 \x01(\x04\",\n\x0cVoteResponse\x12\x0c\n\x04term\x18\x01 \x01(\x04\x12\x0e\n\x06result\x18\x02 \x01(\x08\"\x97\x01\n\rAppendRequest\x12\x12\n\nleaderTerm\x18\x01 \x01(\x04\x12\x10\n\x08leaderId\x18\x02 \x01(\x04\x12\x14\n\x0cprevLogIndex\x18\x03 \x01(\x04\x12\x13\n\x0bprevLogTerm\x18\x04 \x01(\x04\x12\x1a\n\x07\x65ntries\x18\x05 \x03(\x0b\x32\t.LogEntry\x12\x19\n\x11leaderCommitIndex\x18\x06 \x01(\x04\"<\n\x0e\x41ppendResponse\x12\x0c\n\x04term\x18\x01 \x01(\x04\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x0b\n\x03\x61\x63k\x18\x03 \x01(\x04\"\x06\n\x04Void\"8\n\x11GetLeaderResponse\x12\x0e\n\x06nodeId\x18\x01 \x01(\x04\x12\x13\n\x0bnodeAddress\x18\x02 \x01(\t\" \n\x0eSuspendRequest\x12\x0e\n\x06period\x18\x01 \x01(\x04\"\x12\n\x03Key\x12\x0b\n\x03key\x18\x01 \x01(\t\"&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"5\n\x08LogEntry\x12\x1b\n\x08keyValue\x18\x01 \x01(\x0b\x32\t.KeyValue\x12\x0c\n\x04term\x18\x02 \x01(\x04\"!\n\x0eSetValResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"0\n\x0eGetValResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\t2\x85\x02\n\x13RaftElectionService\x12*\n\x0bRequestVote\x12\x0c.VoteRequest\x1a\r.VoteResponse\x12\x30\n\rAppendEntries\x12\x0e.AppendRequest\x1a\x0f.AppendResponse\x12&\n\tGetLeader\x12\x05.Void\x1a\x12.GetLeaderResponse\x12!\n\x07Suspend\x12\x0f.SuspendRequest\x1a\x05.Void\x12$\n\x06SetVal\x12\t.KeyValue\x1a\x0f.SetValResponse\x12\x1f\n\x06GetVal\x12\x04.Key\x1a\x0f.GetValResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VOTEREQUEST']._serialized_start=14
  _globals['_VOTEREQUEST']._serialized_end=114
  _globals['_VOTERESPONSE']._serialized_start=116
  _globals['_VOTERESPONSE']._serialized_end=160
  _globals['_APPENDREQUEST']._serialized_start=163
  _globals['_APPENDREQUEST']._serialized_end=314
  _globals['_APPENDRESPONSE']._serialized_start=316
  _globals['_APPENDRESPONSE']._serialized_end=376
  _globals['_VOID']._serialized_start=378
  _globals['_VOID']._serialized_end=384
  _globals['_GETLEADERRESPONSE']._serialized_start=386
  _globals['_GETLEADERRESPONSE']._serialized_end=442
  _globals['_SUSPENDREQUEST']._serialized_start=444
  _globals['_SUSPENDREQUEST']._serialized_end=476
  _globals['_KEY']._serialized_start=478
  _globals['_KEY']._serialized_end=496
  _globals['_KEYVALUE']._serialized_start=498
  _globals['_KEYVALUE']._serialized_end=536
  _globals['_LOGENTRY']._serialized_start=538
  _globals['_LOGENTRY']._serialized_end=591
  _globals['_SETVALRESPONSE']._serialized_start=593
  _globals['_SETVALRESPONSE']._serialized_end=626
  _globals['_GETVALRESPONSE']._serialized_start=628
  _globals['_GETVALRESPONSE']._serialized_end=676
  _globals['_RAFTELECTIONSERVICE']._serialized_start=679
  _globals['_RAFTELECTIONSERVICE']._serialized_end=940
# @@protoc_insertion_point(module_scope)
