import json
import uuid


class Member:

    def __init__(self, member_uuid: str = None):

        self._uuid: str = str(uuid.uuid4())

        self.name: str = str()
        self.pronouns: str = str()
        self.color_1: str = str()
        self.color_2: str = str()
        self.age: str = str()
        self.age_category: str = str()
        self.role: str = str()
        self.start_tag: str = str()
        self.end_tag: str = str()
        self.typing_quirk: str = str()
        self.description: str = str()
        self.extra_info: str = str()
        self.profile_picture_url: str = str()
        self.banner_url: str = str()

        self._load_data(member_uuid)

    def _load_data(self, member_uuid) -> None:

        # if loading null UUID, return
        if member_uuid is None:
            return

        # if system data not found, return
        if not validate_uuid(member_uuid):
            return

        # load systems data
        with open("data/members.json", "r") as fh:
            members_data = json.load(fh)

        self._uuid = member_uuid

        self.name = members_data[member_uuid]["name"]
        self.pronouns = members_data[member_uuid]["pronouns"]
        self.color_1 = members_data[member_uuid]["color_1"]
        self.color_2 = members_data[member_uuid]["color_2"]
        self.age = members_data[member_uuid]["age"]
        self.age_category = members_data[member_uuid]["age_category"]
        self.role = members_data[member_uuid]["role"]
        self.start_tag = members_data[member_uuid]["start_tag"]
        self.end_tag = members_data[member_uuid]["end_tag"]
        self.typing_quirk = members_data[member_uuid]["typing_quirk"]
        self.description = members_data[member_uuid]["description"]
        self.extra_info = members_data[member_uuid]["extra_info"]
        self.profile_picture_url = members_data[member_uuid]["profile_picture_url"]
        self.banner_url = members_data[member_uuid]["banner_url"]

    def save_data(self):
        with open("data/members.json", "r") as fh:
            members_data = json.load(fh)

        members_data[self._uuid] = {
            "name": self.name,
            "pronouns": self.pronouns,
            "age": self.age,
            "age_category": self.age_category,
            "role": self.role,
            "color_1": self.color_1,
            "color_2": self.color_2,
            "start_tag": self.start_tag,
            "end_tag": self.end_tag,
            "typing_quirk": self.typing_quirk,
            "description": self.description,
            "extra_info": self.extra_info,
            "profile_picture_url": self.profile_picture_url,
            "banner_url": self.banner_url
        }

        with open("data/members.json", "w") as fh:
            json.dump(members_data, fh)

    def get_uuid(self):
        return self._uuid


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

    with open("data/members.json", "r") as fh:
        member_data = json.load(fh)

    return uuid_query in member_data
