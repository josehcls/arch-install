from typing import override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile


class PlasmaProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('Custom KDE Plasma', ProfileType.DesktopEnv)

	@property
	@override
	def packages(self) -> list[str]:
		return [
			'plasma-desktop',
			'kitty',
			'dolphin',
			'ark',
			'sudo',
      'git',
      'neovim',
      'wget',
      'curl',
      'openssh',
      'openvpn',
      'btop',
      'networkmanager',
		]

	@property
	@override
	def default_greeter_type(self) -> GreeterType:
		return GreeterType.Sddm
