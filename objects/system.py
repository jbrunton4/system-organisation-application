import json
from __main__ import objects
from secrets import token_urlsafe

from typing import List


class System:

    def __init__(self, system_uuid: str = None) -> None:
        """
        Constructor for this class
        :param system_uuid: UUID to load data from database. If none given, creates a blank template with new UUID.
        """

        # initialise attributes
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

    def save_data(self) -> None:
        """
        Save this instance's data to the database
        :return: None
        """
        with open("data/systems.json", "r") as fh:
            systems_data = json.load(fh)

        systems_data[self.username] = {
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

    def _load_data(self, username) -> None:
        """
        Given primary key, load data from database
        :param username: Primary key and UUID
        :return: None
        """

        # if loading null UUID, do nothing
        if username is None:
            return

        # if system data not found, return
        if not exists(username):
            return

        # load systems data
        with open("data/systems.json", "r") as fh:
            system_data = json.load(fh)

        # modify instance attributes

        self.username = username
        self.password = system_data[username]["password"]
        self.token = system_data[username]["token"]
        self.name = system_data[username]["name"]
        self.color_1 = system_data[username]["color_1"]
        self.color_2 = system_data[username]["color_2"]
        self.description = system_data[username]["description"]
        self.system_tag = system_data[username]["system_tag"]
        self.profile_picture_url = system_data[username]["profile_picture_url"]
        self.banner_url = system_data[username]["banner_url"]

        self._members = system_data[username]["members"]

    def get_username(self) -> str:
        """
        Getter method for username/UUID
        :return:
        """
        return self.username

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

    def reset_token(self) -> None:
        """
        Generates a new 64-byte URL safe token and saves
        :return: None
        """
        self.token = token_urlsafe(64)
        self.save_data()

    def validate_token(self, token_attempt) -> bool:
        """
        Validate a token for this instance
        :param token_attempt: The token attempt to check against the token
        :return: True if tokens match else False
        """
        return token_attempt == self.token

    def get_uuid(self) -> str:
        """
        Alias for system.username
        :return: system.username
        """
        return self.username


class SystemNotFoundException(Exception):
    """
    Exception raised when a system is not found in the database.
    """

    def __init__(self, system_uuid: str) -> None:
        super().__init__(f"The member UUID \"{system_uuid}\" was not found in the database.")


def exists(username: str) -> bool:
    """
    Check if a primary key is present in the database
    :param username: The primary key to check for
    :return: True if present else False
    """
    with open("data/systems.json", "r") as fh:
        system_data = json.load(fh)

    return username in system_data
