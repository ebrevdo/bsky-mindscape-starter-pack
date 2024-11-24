import os

from atproto import Client, models
from atproto_client.client.session import Session

SESSION_FILE = os.path.expanduser("~/atproto_session.txt")
if not os.path.exists(SESSION_FILE):
    raise RuntimeError(f"First run python login_atproto.py to create {SESSION_FILE}")

with open(SESSION_FILE, "r") as f:
    session_string = f.read()

client = Client()
client.login(session_string=session_string)
session = Session.decode(session_string)

list_of_starter_packs = client.com.atproto.repo.list_records(
    models.ComAtprotoRepoListRecords.Params(
        repo=client.me.did, collection=models.ids.AppBskyGraphStarterpack
    )
)
starter_pack_0 = list_of_starter_packs.records[0]
# get the list from the starter pack
starter_pack_0_list_at_uri = starter_pack_0.value.list
starter_pack_0_list_rkey = starter_pack_0_list_at_uri.split("/")[-1]
# get the list from the starter pack
starter_pack_0_list = client.com.atproto.repo.get_record(
    models.ComAtprotoRepoGetRecord.Params(
        repo=client.me.did,
        collection=models.ids.AppBskyGraphList,
        rkey=starter_pack_0_list_rkey,
    )
)

sp = client.app.bsky.graph.get_starter_pack(
    models.AppBskyGraphGetStarterPack.Params(starter_pack=starter_pack_0.uri)
)
list_uri = sp.starter_pack.list.uri
sp_list = client.app.bsky.graph.get_list(models.AppBskyGraphGetList.Params(list=list_uri))


# starter_pack_0_list_cid = starter_pack_0_list.cid
# starter_pack_0_list_value = starter_pack_0_list.value
# # get the list from the starter pack
# starter_pack_0_list_value_records = starter_pack_0_list_value.records

breakpoint()

r = client.com.atproto.repo.create_record(
    models.ComAtprotoRepoCreateRecord.Data(
        repo=client.me.did,
        collection=models.ids.AppBskyGraphStarterpack,
        record=models.AppBskyGraphStarterpack.Record(
            created_at=client.get_current_time_iso(), name="test", description="test", list=""
        ),
    )
)

breakpoint()
