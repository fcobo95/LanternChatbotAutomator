from watson_developer_cloud import ConversationV1 as Conversation
import json


class Synonym:
    """
    DOCSTRING
    """

    def __init__(self, username=None, password=None, version=None):
        self.conversation = Conversation(
            username=username,  # '46b3dba5-3f3e-4b04-b8f2-38e65eaefe1a',
            password=password,  # "7Q3xmUgDqYxM",
            version=version  # "2017-05-26"
        )

    def get_all_synonyms(self, workspace_id, entity, value, page_limit, include_count, sort, cursor):
        response = self.conversation.list_synonyms(
            workspace_id=workspace_id,
            entity=entity,
            value=value,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor
        )
        print(json.dumps(response, indent=2))

    def create_synonym(self, workspace_id, entity, value, synonym):
        response = self.conversation.create_synonym(
            workspace_id=workspace_id,
            entity=entity,
            value=value,
            synonym=synonym
        )
        print(json.dumps(response, indent=2))

    def delete_synoym(self, workspace_id, entity, value, synonym):
        self.conversation.delete_synonym(
            workspace_id=workspace_id,
            entity=entity,
            value=value,
            synonym=synonym
        )
        print("Deleted synonym {} from entity {}".format(synonym, entity))

    def get_synonym(self, workspace_id, entity, value, synonym):
        response = self.conversation.get_synonym(
            workspace_id=workspace_id,
            entity=entity,
            value=value,
            synonym=synonym
        )
        print(json.dumps(response, indent=2))

    def update_synonym(self, workspace_id, entity, value, synonym, new_synonym):
        response = self.conversation.update_synonym(
            workspace_id=workspace_id,
            entity=entity,
            value=value,
            synonym=synonym,
            new_synonym=new_synonym
        )
        print(json.dumps(response, indent=2))
