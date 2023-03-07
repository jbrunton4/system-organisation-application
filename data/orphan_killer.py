import json
from objects.system import System
from objects.member import Member
from tqdm import tqdm


def kill_orphans() -> None:
    """
    Script to delete all members that are not part of any system
    :return: None
    """

    with open("data/members.json", "r") as fh:
        member_data = json.load(fh)
        members = list(json.load(fh).keys())

    used_members = []
    with open("data/systems.json", "r") as fh:
        system_data = json.load(fh)

        for system in system_data:
            for member in System(system).get_members():
                used_members.append(member)

        del system_data

    n_killed = 0
    for member in tqdm(members):
        if member not in used_members:
            del member_data[member]
            n_killed += 1
    print(f"Killed {n_killed} orphans")
