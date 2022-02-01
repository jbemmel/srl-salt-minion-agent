#!/usr/bin/env python
# coding=utf-8

import grpc

from datetime import datetime

from ndk import sdk_service_pb2,sdk_service_pb2_grpc

import logging
from logging.handlers import RotatingFileHandler

# Salt specific
from salt.minion import Minion
from salt.config import DEFAULT_MINION_OPTS

agent_name = "srl-salty-minion-agent"


if __name__ == "__main__":

    log_filename = f"/var/log/srlinux/stdout/{agent_name}.log"
    logging.basicConfig(
        handlers=[RotatingFileHandler(log_filename, maxBytes=3000000, backupCount=5)],
        format="%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )
    logging.info("START TIME :: {}".format(datetime.now()))

    channel = grpc.insecure_channel("127.0.0.1:50053")
    metadata = [("agent_name", agent_name)]
    sdk_mgr_client = sdk_service_pb2_grpc.SdkMgrServiceStub(channel)

    response = sdk_mgr_client.AgentRegister(
        request=sdk_service_pb2.AgentRegistrationRequest(), metadata=metadata
    )
    logging.info(f"Agent succesfully registered! App ID: {response.app_id}")

    opts = { **DEFAULT_MINION_OPTS,
             'master': '172.20.20.10',
             'id': '007','autosign_grains': ['id'],
             '__role': 'minion'
           }
    try:
      m = Minion( opts=opts )
      m.sync_connect_master()
      logging.info( "Minion connected to master" )
    except Exception as ex:
      logging.error(ex)
