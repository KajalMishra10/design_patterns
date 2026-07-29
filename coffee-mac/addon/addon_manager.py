from addon.addon import Addon


class AddonManager:

    def __init__(self):
        self._addons = {}
        self.add_addon(Addon("Extra Sugar", 5))
        self.add_addon(Addon("Extra Milk", 10))

    def add_addon(self, addon: Addon):
        self._addons[addon.name] = addon

    def get_addon(self, name):
        return self._addons.get(name)

    def is_addon_available(self, name):
        return name in self._addons

    def validate_addons(self, addon_names):

        if not addon_names:
            return True

        for addon_name in addon_names:
            if addon_name not in self._addons:
                print(f"{addon_name} is not supported.")
                return False

        return True

    def get_total_addon_price(self, addon_names):

        total = 0

        if not addon_names:
            return total

        for addon_name in addon_names:
            total += self._addons[addon_name].price

        return total