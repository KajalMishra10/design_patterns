from addon.addon import Addon


class AddonManager:

    DEFAULT_ADDONS = [
    Addon("Extra Sugar", 5),
    Addon("Extra Milk", 10),
    ]

    def __init__(self):
        self._addons = {}
        for addon in self.DEFAULT_ADDONS:
            self.add_addon(addon)

    def add_addon(self, addon: Addon):
        self._addons[addon.name] = addon

    def get_addon(self, name):
        if name not in self._addons:
            raise ValueError(f"{name} is not supported.")

        return self._addons[name]

    def validate_addons(self, addon_names):

        if not addon_names:
            return True

        for addon_name in addon_names:
            if addon_name not in self._addons:
                print(f"{addon_name} is not supported.")
                return False

        return True

 #   def get_total_addon_price(self, addon_names):

  #      total = 0

   #     if not addon_names:
    #        return total
#
 #       for addon_name in addon_names:
  #          total += self._addons[addon_name].price

  #      return total