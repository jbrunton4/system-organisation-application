import json
import uuid
from __main__ import objects
from secrets import token_urlsafe

from typing import List


class System:

    def __init__(self, system_uuid: str = None):

        # initialise attributes
        self._uuid: str = str(uuid.uuid4())

        self.username: str = str()
        self.password: str = str()
        self.token: str = str(token_urlsafe(64))
        self.color_1: str = "#000000"
        self.color_2: str = "#ffffff"
        self.name: str = str()
        self.description: str = str()
        self.system_tag: str = str()
        self.profile_picture_url: str = str()
        self.banner_url: str = str()

        self._members: List[str] = []

        # if a valid UUID is passed, load data
        self._load_data(system_uuid)

    def save_data(self):
        with open("data/systems.json", "r") as fh:
            systems_data = json.load(fh)

        systems_data[self._uuid] = {
            "username": self.username,
            "password": self.password,
            "token": self.token,
            "color_1": self.color_1,
            "color_2": self.color_2,
            "name": self.name,
            "members": self._members,
            "description": self.description,
            "system_tag": self.system_tag,
            "profile_picture_url": self.profile_picture_url,
            "banner_url": self.banner_url
        }

        with open("data/systems.json", "w") as fh:
            json.dump(systems_data, fh)

    def _load_data(self, system_uuid) -> None:

        # if loading null UUID, return
        if system_uuid is None:
            return

        # if system data not found, return
        if not validate_uuid(system_uuid):
            return

        # load systems data
        with open("data/systems.json", "r") as fh:
            system_data = json.load(fh)

        # modify instance attributes
        self._uuid = system_uuid

        self.username = system_data[system_uuid]["username"]
        self.password = system_data[system_uuid]["password"]
        self.token = system_data[system_uuid]["token"]
        self.name = system_data[system_uuid]["name"]
        self.color_1 = system_data[system_uuid]["color_1"]
        self.color_2 = system_data[system_uuid]["color_2"]
        self.description = system_data[system_uuid]["description"]
        self.system_tag = system_data[system_uuid]["system_tag"]
        self.profile_picture_url = system_data[system_uuid]["profile_picture_url"]
        self.banner_url = system_data[system_uuid]["banner_url"]

        self._members = system_data[system_uuid]["members"]

    def get_uuid(self) -> str:
        return self._uuid

    def get_members(self) -> List[str]:
        """
        Get a list of the UUIDs of this system's members
        :return: A list of UUIDs as strings
        """
        return self._members

    def add_member(self, member_uuid: str) -> None:
        """
        Add a member UUID to this system's member list
        :param member_uuid: The member UUID to add
        :return: None
        """
        if not objects.member.validate_uuid(member_uuid):
            raise objects.member.MemberNotFoundException(member_uuid)
        self._members.append(member_uuid)

    def remove_member(self, member_uuid: str) -> None:
        """
        Remove a member UUID from this system's member list.
        If the UUID does not exist in the list, the method works as normal.
        :param member_uuid: The UUID to remove
        :return: None
        """
        self._members.remove(member_uuid)


class SystemNotFoundException(Exception):
    """
    Exception raised when a system is not found in the database.
    """

    def __init__(self, system_uuid: str):
        super().__init__(f"The member UUID \"{system_uuid}\" was not found in the database.")


def exists(name: str) -> bool:
    with open("data/systems.json", "r") as fh:
        member_data = json.load(fh)

    for m in member_data:
        if System(m).name == name:
            return True
    return False


def validate_uuid(uuid_query: str) -> bool:
    """
    Validate a UUID.
    :return: True if UUID exists else False
    """

    with open("data/systems.json", "r") as fh:
        system_data = json.load(fh)

    return uuid_query in system_data
