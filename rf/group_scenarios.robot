*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add group
    ${old_list}  Get Group List
    ${group}  New Group  rf_name  rf_header  rf_footer
    Create Group  ${group}
    Append To List  ${old_list}  ${group}
    ${new_list}  Get Group List
    Group Lists Equal  ${old_list}  ${new_list}

Modify group
    Ensure Group Exists
    ${old_list}  Get Group List
    ${group_to_modify}  Random Entity  ${old_list}
    ${new_data}  New Group  fr_name_upd  fr_head_upd  fr_foot_upd
    Modify Group  ${group_to_modify}  ${new_data}
    Remove Values From List  ${old_list}  ${group_to_modify}
    Append To List  ${old_list}  ${new_data}
    ${new_list}  Get Group List
    Group Lists Equal  ${old_list}  ${new_list}

Delete group
    Ensure Group Exists
    ${old_list}  Get Group List
    ${len}  Get Length  ${old_list}
    ${index}  Evaluate  random.randrange(${len})  random
    ${group}  Get From List  ${old_list}  ${index}
    Delete Group  ${group}
    Remove Values From List  ${old_list}  ${group}
    ${new_list}  Get Group List
    Group Lists Equal  ${old_list}  ${new_list}