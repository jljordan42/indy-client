from plenum.cli.constants import CLIENT_GRAMS_CLIENT_COMMAND_REG_EX, relist, \
    CLI_CMDS, getPipedRegEx, CLIENT_GRAMS_USE_KEYPAIR_REG_EX
from sovrin_common.roles import Roles
from sovrin_common.transactions import SovrinTransactions

CLIENT_GRAMS_CLIENT_WITH_IDENTIFIER_FORMATTED_REG_EX = getPipedRegEx(
    CLIENT_GRAMS_CLIENT_COMMAND_REG_EX +
    "\s+ (?P<with_identifier>with\s+identifier) "
    "\s+ (?P<nym>[a-zA-Z0-9=]+) \s*") \
    .format(relist(CLI_CMDS))

CLIENT_GRAMS_CLIENT_ADD_FORMATTED_REG_EX = getPipedRegEx(
    "(\s* (?P<client>client) \s+ (?P<client_name>[a-zA-Z0-9]+) "
    "\s+ (?P<cli_action>add) \s+ (?P<role>{trustAnchor}|user) "
    "\s+ (?P<other_client_name>[a-zA-Z0-9]+) \s*)".format(trustAnchor=Roles.TRUST_ANCHOR.name))

CLIENT_GRAMS_USE_KEYPAIR_FORMATTED_REG_EX = getPipedRegEx(
    CLIENT_GRAMS_USE_KEYPAIR_REG_EX)

# TODO we can genericize the other TXN types in the same way
TXN_NYM = "(\s* (?P<{{cmdName}}>{{cmd}}\s+{nym}) " \
          "\s+ (?P<dest>dest=) \s* (?P<dest_id>[A-Za-z0-9+=/]*)" \
          "(\s+ (?P<role_key>role=) \s* (?P<role>{trustee}|{tgb}|{trustAnchor}|{steward}|))?" \
          "(\s+ (?P<ver_key>verkey=) \s* (?P<new_ver_key>[~A-Za-z0-9+=/]+))?)".format(nym=SovrinTransactions.NYM.name,
                                                                                      trustee=Roles.TRUSTEE.name,
                                                                                      tgb=Roles.TGB.name,
                                                                                      trustAnchor=Roles.TRUST_ANCHOR.name,
                                                                                      steward=Roles.STEWARD.name)

SEND_NYM_REG_EX = TXN_NYM.format(cmdName='send_nym', cmd='send')

ADD_GENESIS_NYM_REG_EX = TXN_NYM.format(cmdName='add_genesis',
                                        cmd='add \s+ genesis \s+ transaction')

NEW_ID_REG_EX = "(\s* (?P<new_id>new\s+identifier)" \
                "\s? (?P<id_or_abbr_or_crypto>([A-Za-z0-9+=/]+|abbr|crypto))? " \
                "\s? (with\s+seed\s+(?P<seed>[a-zA-Z0-9]+))? " \
                "\s? (as\s+(?P<alias>[a-zA-Z0-9-]+))?)"

GET_NYM_REG_EX = "(\s* (?P<send_get_nym>send\s+{getNym}) " \
                 "\s+ (?P<dest>dest=)\s*(?P<dest_id>[A-Za-z0-9+=/]+) \s*) ".format(
    getNym=SovrinTransactions.GET_NYM.name)

ADD_ATTRIB_REG_EX = \
    "(\s* (?P<send_attrib>send\s+{attrib}) " \
    "\s+ dest=\s*(?P<dest_id>[A-Za-z0-9+=/]+) " \
    "\s+ raw=(?P<raw>\{{\s*.*\}}) \s*) ".format(attrib=SovrinTransactions.ATTRIB.name)

SEND_SCHEMA_REG_EX = "(\s*(?P<send_schema>send\s+{schema})" \
                     "\s+(?P<name_key>name=)\s*(?P<name>[A-Za-z0-9-_]+)" \
                     "\s*(?P<version_key>version=)\s*(?P<version>[0-9.]+)" \
                     "\s+(?P<keys_key>keys=)\s*(?P<keys>[0-9a-zA-Z-_,\s]+)\s*)".format(
    schema=SovrinTransactions.SCHEMA.name)

SEND_CLAIM_DEF_REG_EX = "(\s*(?P<send_claim_def>send\s+{issKey})" \
                        "\s+(?P<ref_key>ref=)\s*(?P<ref>[0-9]+)\s*)"\
                        "\s*(?P<signature_type_key>signature_type=)\s*(?P<signature_type>[A-Z0-9]+)" \
    .format(issKey=SovrinTransactions.CLAIM_DEF.name)


ADD_ATTRS_PROVER_REG_EX = "(\s*(?P<add_attrs>attribute \s+ known \s+ to) " \
                          "\s+ (?P<issuer_id>[A-Za-z0-9+=/]+) " \
                          "\s+ (?P<attrs>[A-Za-z0-9_,+=/ ]+) \s*)"

INIT_ATTR_REPO_REG_EX = "(\s*(?P<init_attr_repo>initialize " \
                        "\s+ mock \s+ attribute \s+ repo)\s*)"

ADD_ATTRS_REG_EX = "(\s*(?P<add_attrs>add \s+ attribute) " \
                   "\s+ (?P<attrs>[A-Za-z0-9_,+=/ ]+) " \
                   "\s+ for \s+ (?P<prover_id>[a-zA-Z0-9\-_]+) \s*)"

SHOW_FILE_REG_EX = "(\s*(?P<show_file>show) " \
                   "\s+ (?P<file_path>[A-Za-z0-9+-.=/]+)\s*)"

CONNECT_REG_EX = "(\s*(?P<conn>connect) \s+ (?P<env_name>[A-Za-z0-9-]+)\s*)"

DISCONNECT_REG_EX = "(\s*(?P<disconn>disconnect))"

LOAD_FILE_REG_EX = "(\s*(?P<load_file>load) " \
                   "\s+ (?P<file_path>[A-Za-z0-9+-.=/]+)\s*)"

SHOW_LINK_REG_EX = '(\s*(?P<show_link>show \s+ link) ' \
                   '\s+ (?P<link_name>[A-Za-z0-9-." ]+) \s*)'

SYNC_LINK_REG_EX = '(\s*(?P<sync_link>sync) ' \
                   '\s+ (?P<link_name>[A-Za-z0-9-." ]+) \s*)'

PING_TARGET_REG_EX = '(\s*(?P<ping>ping) ' \
                     '\s+ (?P<target_name>[A-Za-z0-9-." ]+) \s*)'

ACCEPT_LINK_REG_EX = \
    '(\s*(?P<accept_link_invite>accept \s+ invitation \s+ from) ' \
    '\s+ (?P<link_name>[A-Za-z0-9-." ]+) \s*)'

SHOW_CLAIM_REG_EX = '(\s*(?P<show_claim>show \s+ claim) ' \
                    '\s+ (?P<claim_name>[A-Za-z0-9-." ]+) ' \
                    '\s*)'

LIST_CLAIMS_REG_EX = '(\s*(?P<list_claims>list \s+ claims) ' \
                     '\s+ (?P<link_name>[A-Za-z0-9-." ]+) \s*)'

LIST_LINKS_REG_EX = '(\s*(?P<list_links>list \s+ links))'

REQUEST_CLAIM_REG_EX = '(\s*(?P<req_claim>request \s+ claim) ' \
                       '\s+ (?P<claim_name>[A-Za-z0-9-." ]+) ' \
                       '\s*)'

# SHOW_CLAIM_REQ_REG_EX = '(\s*(?P<show_claim_req>show \s+ claim \s+ request) ' \
#                     '\s+ (?P<claim_req_name>[A-Za-z0-9-." ]+) ' \
#                     '\s*)'
#
SHOW_PROOF_REQ_REG_EX = '(\s*(?P<show_proof_req>show \s+ proof \s+ request) ' \
                        '\s+ (?P<proof_req_name>[A-Za-z0-9-." ]+) ' \
                        '\s*)'

SET_ATTRIBUTE_REG_EX = '(\s*(?P<set_attr>set) ' \
                       '\s+ (?P<attr_name>[A-Za-z-_0-9]+) ' \
                       '\s+ to \s+ (?P<attr_value>[A-Za-z0-9+-_,." /]+)' \
                       '\s*)'

SEND_PROOF_REG_EX = '(\s*(?P<send_proof>send \s+ proof) ' \
                    '\s+ (?P<proof_name>[A-Za-z0-9-." ]+) ' \
                    '\s+ to \s+ (?P<link_name>[A-Za-z0-9-." ]+) \s*)'

SEND_PROOF_REQ_REG_EX = '(\s*(?P<send_proof_req>send \s+ proof-request) ' \
                    '\s+ (?P<proof_request_name>[A-Za-z0-9-." ]+) ' \
                    '\s+ to (?P<target>[A-Za-z0-9-." ]+) \s*)'

SEND_NODE_REG_EX = "(\s* (?P<send_node>send\s+{node}) " \
                   "\s+ dest=\s*(?P<dest_id>[A-Za-z0-9+/]+) " \
                   "\s+ data=(?P<data>\{{\s*.*\}}) \s*) ".format(node=SovrinTransactions.NODE.name)

SEND_POOL_UPG_REG_EX = "(\s*(?P<send_pool_upg>send\s+{poolUpgrade})" \
                       "\s+(?P<name_key>name=)\s*(?P<name>[A-Za-z0-9-_]+)" \
                       "\s*(?P<version_key>version=)\s*(?P<version>[0-9.]+)" \
                       "\s*(?P<sha256_key>sha256=)\s*(?P<sha256>[a-f0-9]+)" \
                       "(\s+ (?P<action_key>action=)\s*(?P<action>start|cancel))" \
                       '(\s+ (?P<justification_key>justification=)\s*(?P<justification>\"[a-zA-z0-9-_\s]+\") \s*)? ' \
                       "(\s+ (?P<schedule_key>schedule=)\s*(?P<schedule>\{{\s*.*\}}) \s*)? " \
                       "(\s+ (?P<timeout_key>timeout=)\s*(?P<timeout>[0-9+]+))?)".format(poolUpgrade=SovrinTransactions.POOL_UPGRADE.name)

REQ_AVAIL_CLAIMS_REG_EX = '(\s*(?P<req_avail_claims>request \s+ available \s+ claims \s+ from) ' \
                          '\s+ (?P<link_name>[A-Za-z0-9-." ]+) \s*)'

SEND_NYM_FORMATTED_REG_EX = getPipedRegEx(SEND_NYM_REG_EX)
GET_NYM_FORMATTED_REG_EX = getPipedRegEx(GET_NYM_REG_EX)
ADD_ATTRIB_FORMATTED_REG_EX = getPipedRegEx(ADD_ATTRIB_REG_EX)
SEND_SCHEMA_FORMATTED_REG_EX = getPipedRegEx(SEND_SCHEMA_REG_EX)
SEND_CLAIM_DEF_FORMATTED_REG_EX = getPipedRegEx(SEND_CLAIM_DEF_REG_EX)
ADD_GENESIS_FORMATTED_REG_EX = getPipedRegEx(ADD_GENESIS_NYM_REG_EX)
INIT_ATTR_REPO_FORMATTED_REG_EX = getPipedRegEx(INIT_ATTR_REPO_REG_EX)
ADD_ATTRS_FORMATTED_REG_EX = getPipedRegEx(ADD_ATTRS_REG_EX)
SHOW_FILE_FORMATTED_REG_EX = getPipedRegEx(SHOW_FILE_REG_EX)
LOAD_FILE_FORMATTED_REG_EX = getPipedRegEx(LOAD_FILE_REG_EX)
SHOW_LINK_FORMATTED_REG_EX = getPipedRegEx(SHOW_LINK_REG_EX)
ADD_ATTRS_PROVER_FORMATTED_REG_EX = getPipedRegEx(ADD_ATTRS_PROVER_REG_EX)
CONNECT_FORMATTED_REG_EX = getPipedRegEx(CONNECT_REG_EX)
DISCONNECT_FORMATTED_REG_EX = getPipedRegEx(DISCONNECT_REG_EX)
SYNC_LINK_FORMATTED_REG_EX = getPipedRegEx(SYNC_LINK_REG_EX)
ACCEPT_LINK_FORMATTED_REG_EX = getPipedRegEx(ACCEPT_LINK_REG_EX)
SHOW_CLAIM_FORMATTED_REG_EX = getPipedRegEx(SHOW_CLAIM_REG_EX)
LIST_CLAIMS_FORMATTED_REG_EX = getPipedRegEx(LIST_CLAIMS_REG_EX)
LIST_LINKS_FORMATTED_REG_EX = getPipedRegEx(LIST_LINKS_REG_EX)
REQUEST_CLAIM_FORMATTED_REG_EX = getPipedRegEx(REQUEST_CLAIM_REG_EX)
# SHOW_CLAIM_REQ_FORMATTED_REG_EX = getPipedRegEx(SHOW_CLAIM_REQ_REG_EX)
SHOW_PROOF_REQ_FORMATTED_REG_EX = getPipedRegEx(SHOW_PROOF_REQ_REG_EX)
SET_ATTRIBUTE_FORMATTED_REG_EX = getPipedRegEx(SET_ATTRIBUTE_REG_EX)
PING_TARGET_FORMATTED_REG_EX = getPipedRegEx(PING_TARGET_REG_EX)
SEND_PROOF_FORMATTED_REG_EX = getPipedRegEx(SEND_PROOF_REG_EX)
SEND_PROOF_REQ_FORMATTED_REG_EX = getPipedRegEx(SEND_PROOF_REQ_REG_EX)
SEND_NODE_FORMATTED_REG_EX = getPipedRegEx(SEND_NODE_REG_EX)
SEND_POOL_UPG_FORMATTED_REG_EX = getPipedRegEx(SEND_POOL_UPG_REG_EX)
REQ_AVAIL_CLAIMS_FORMATTED_REG_EX = getPipedRegEx(REQ_AVAIL_CLAIMS_REG_EX)
NEW_ID_FORMATTED_REG_EX = getPipedRegEx(NEW_ID_REG_EX)
