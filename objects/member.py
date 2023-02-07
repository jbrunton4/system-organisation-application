import json



class Member:

    def __init__(self):
        self._name: str = str()
        self._pronouns: str = str()
        self._age: str = str()
        self._age_category: str = str()
        self._role: str = str()
        self._proxy_tags: str = str()
        self._typing_quirk: str = str()
        self._description: str = str()
        self._extra_info: str = str()

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_pronouns(self) -> str:
        return self._pronouns

    def set_pronouns(self, pronouns: str) -> None:
        self._pronouns = pronouns

    def get_age(self) -> str:
        return self._age

    def set_age(self, age: str) -> None:
        self._age = age

    def get_age_category(self) -> str:
        return self._age_category

    def set_age_category(self, age_category: str) -> None:
        self._age_category = age_category

    def get_role(self) -> str:
        return self._role

    def set_role(self, role: str) -> None:
        self._role = role

    def get_proxy_tags(self) -> str:
        return self._proxy_tags

    def set_proxy_tags(self, proxy_tags: str) -> None:
        self._proxy_tags = proxy_tags

    def get_typing_quirk(self) -> str:
        return self._typing_quirk

    def set_typing_quirk(self, typing_quirk: str) -> None:
        self._typing_quirk = typing_quirk

    def get_description(self) -> str:
        return self._description

    def set_description(self, description: str) -> None:
        self._description = description

    def get_extra_info(self) -> str:
        return self._extra_info

    def set_extra_info(self, extra_info: str) -> None:
        self._extra_info = extra_info


class MemberNotFoundException(Exception):
    """
    Exception raised when a member is not found in the database.
    """

    def __init__(self, member_uuid: str):
        super().__init__(f"The member UUID \"{member_uuid}\" was not found in the database.")


def validate_uuid(uuid_query: str) -> bool:
    """
    Validate a UUID.
    :return: True if UUID exists else False
    """

    with open("members.json", "r") as fh:
        member_data = json.load(fh)

    return uuid_query in member_data
