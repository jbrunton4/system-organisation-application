import json
import uuid
from __main__ import objects

from typing import List


class System:

    def __init__(self, system_uuid: str = None):

        # initialise attributes
        self._uuid: str = str(uuid.uuid4())
        self._name: str = str()
        self._members: List[str] = []
        self._description: str = str()

        # if a valid UUID is passed, load data
        self._load_data(system_uuid)

    def _save_data(self):
        with open("systems.json", "r") as fh:
            systems_data = json.load(fh)

        systems_data[self._uuid] = {
            "name": self._name,
            "members": self._members,
            "description": self._description,
        }

    def _load_data(self, system_uuid) -> None:

        # if loading null UUID, return
        if system_uuid is None:
            return

        # if system data not found, return
        if not validate_uuid(system_uuid):
            return

        # load systems data
        with open("systems.json", "r") as fh:
            system_data = json.load(fh)

        # modify instance attributes
        self._uuid = system_uuid
        self._name = system_data[system_uuid]["name"]
        self._members = system_data[system_uuid]["members"]
        self._description = system_data[system_uuid]["description"]

    def get_name(self) -> str:
        """
        Get a system's name/title
        :return: This instance's name attribute
        """
        return self._name

    def set_name(self, name: str) -> None:
        """
        Sets the system's name/title
        :param name: The new name to set
        :return: None
        """
        self._name = name

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


def validate_uuid(uuid_query: str) -> bool:
    """
    Validate a UUID.
    :return: True if UUID exists else False
    """

    with open("systems.json", "r") as fh:
        member_data = json.load(fh)

    return uuid_query in member_data
