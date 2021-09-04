# Dotfiles

## Introduction
A repository contains backups of my Debian configurations to make myself easier
to recreate my setup on a new OS install.

## Software I use
- **Distro** Debian 11
- **Display Server** X11
- **Display Manager** Slim

![](https://i.imgur.com/nUNa3Ws.png)

- **Desktop Environment** None
- **WM** Bspwm

![](https://i.imgur.com/PejIq3q.png)

Simple configuration with only 11 lines of `bspc config`
and 24 lines of window rules.
And I try to make my Bspwm setup comfortably usable on both keyboard and mouse.

- **Panel** Polybar
- **Launcher** Rofi

![](https://i.imgur.com/cmQFJji.png)

- **Lock Screen** i3lock

![](https://i.imgur.com/5QaNc7i.png)

Clean sample without any window opened.

![](https://i.imgur.com/8FQPdCP.png)

Dirty sample with some windows opened.
Not good for hiding sensitive image or video.

- **Terminal** Kitty
- **Task Manager** HTOP

![](https://i.imgur.com/WZ4qNqd.png)

- **Power Manager** TLP
- **Sound Mixer** PulseAudio

I have tried to use pure ALSA without PulseAudio, but it made my
life harder. When I attached my headphone, the speaker was still on.
I needed to turn the speaker off manually from `alsamixer` command.
Better to use PulseAudio to make my life easier.

- **Policy Kit Frontend** Gnome Polkit
- **Notification Daemon** Dunst

![](https://i.imgur.com/LRpg6i9.png)

- **Pager** Less
- **CLI Shell** Fish

I have written an article about fish
[here](https://addy-dclxvi.github.io/post/fish-shell/)

- **CLI File Manager** Ranger

![](https://i.imgur.com/32ylsaf.png)

Highlight feature in Ranger

![](https://i.imgur.com/SvdZAmD.png)

Tinkering with Ranger colorscheme

- **CLI Image Viewer** Caca

![](https://i.imgur.com/kgjxR5B.png)

I use Caca as terminal image previewer in Ranger.
That's a photo of me and my friends at Mount Bromo, East Java.

- **CLI Text Editor** Neovim

![](https://i.imgur.com/8AVGrcH.png)

I'm not a programmer. So my Neovim configuration is pretty simple,
centralized in `~/.config/nvim/init.vim`. Not many plugins installed.
Only statusline, syntax checker, auto completion, and hex code colorizer.
I save a copy of the plugins in this repository to make me easier recreating
this setup on a freshly installed machine. They are placed in
`~/.config/nvim/` and `~/.local/share/nvim/`.

![](https://i.imgur.com/4deA5tS.png)

![](https://i.imgur.com/53DybwS.png)

![](https://i.imgur.com/ZL25J8j.png)

My keymap is uncommon for Neovim.
I map **Ctrl + Space** for next auto completion,
**Ctrl + Backspace** delete per word.
**Ctrl + S** save.
**Ctrl + Z** undo.
**Ctrl + Y** redo.
**Ctrl + Arrows** jump. And many others.
Because if the default vim keybinding mapped permanently in my fingers,
it makes me hard to survive in non-vi style apps.
Once I tried to navigate a Spreadseet using H-J-K-L
and tried to quit Writer by typing <Esc> :wq <Enter>.

- **GUI Text Editor** Geany
- **Image Viewer** Viewnior
- **Screenshooter** scrot

![](https://i.imgur.com/cQ2RE2z.png)

I set the **PrtSc** key to take screenshot using scrot,
then instantly preview the result using default image viewer.
So I can hit the delete button in my keyboard if unsatisfied
with the result. Or, right click on the image then select open with GIMP,
to instantly edit it using GIMP without opening the file manager.

- **Wallpaper Handler** hsetroot
- **Brightness Manager** xbacklight
- **Music Player** Cmus

![](https://i.imgur.com/cNhJJhn.png)

Tree/Library Mode (Num 1)

![](https://i.imgur.com/UIZdICk.png)

Playlist Mode (Num 2)

![](https://i.imgur.com/KfA8UKy.png)

File Browser Mode (Num 5)

Cmus is a also good for online radio stream.
The artist and song title is displayed correctly.
I save a copy of online radio stream files in this repository,
in `~/Music` folder.

> *Why don't you use Spotify like normal people do?*

Because Spotify recommendation playlist is not designed for
Progressive / Extreme / Technical Death Metal fans.
Listening radio is better for music discovery.
I can find many underrated artists and songs from radio.

- **Compositor** Compton
- **Hardware Acceleration Driver** i965-va-driver
- **Encoder/Decoder** ffmpeg
- **Media Player** MPV

![](https://i.imgur.com/CZkrpsS.png)

> *Gentlemen, welcome to Arch Club.*
> *The first rule of Arch Club is you tell everyone you use Arch.*
> *The second rule of Arch Club is YOU HAVE TO TELL EVERYONE you use Arch!!*
> *Third rule of Arch Club, Someone yells "Install Gentoo!", goes limp, taps out,*
> *the install is over. Fourth rule, only one guy to an install.*
> *Fifth rule, one install at a time, fellas. Sixth rule, No YouTube tutorial,*
> *no blogger tutorial. Seventh rule, install will go on as long as they have to.*
> *And the eighth and final rule, If this is your first night at Arch Club,*
> *you have to install Arch!*


![](https://i.imgur.com/E1nOJiE.png)

Steins;Gate

![](https://i.imgur.com/eHbmzeT.png)

Suckseed

![](https://i.imgur.com/NPGzAvy.png)

MPV can stream URL too.
In example above, I stream a YouTube video from Kurzgesagt channel.

- **GTK Theme** Materia-light

I prefer to use a light GTK theme. Even if I use a dark GTK theme,
the GIMP canvas, Libreoffice paper, ebook background, will be still white.
The internet is also white. Causing my eyes to work harder.
So better to use a light theme for GTK for a better readability.
 
- **Icons** Faba
- **File Manager** Nautilus

![](https://i.imgur.com/PBNhpEy.png)

Usually I use Thunar.
But after Thunar migrated to GTK3, I feel it heavier.
I tried PCManFM and SpaceFM but did not feel comfortable.
So I try Nautilus, and it actually not heavy if it runs without GNOME.
And with `--no-install-recommends` flag when installing,
It only pulls a small amount of GNOME dependencies.
Just like Thunar pulls some XFCE dependencies.
Also, I have pulled other component of GNOME Desktop,
like Evince, File Roller, GVFS, Pavucontrol, and GNOME Polkit anyway.
Utilization of shared dependencies will make my setup has
a smaller footprint.

- **Archive Manager** File Roller
- **PDF Reader** Evince

![](https://i.imgur.com/XINPsbg.png)

I choose Evince because it has DJVU support out the box.
I can use it as ebook reader.

The Murder of Roger Ackroyd by Agatha Christie is one of the best book I ever read.
I still can't believe the ending. It can't be possible.
I have been tricked for 26 chapters.

- **Web Browser** Firefox

![](https://i.imgur.com/1USbRal.png)

Nothing special here. Default config.

![](https://i.imgur.com/Tm2x0gM.png)

JoJo's Part IV: Debian is Unbreakable

When you are so overpowered. You forget that you are no longer the main
protagonist in this part, and keep beating the main villain.

- **Spreadseet** Libreoffice Calc

![](https://i.imgur.com/eZ2kyl1.png)

- **Word Processor** Libreoffice Writer

![](https://i.imgur.com/UsWzYH1.png)

- **Libreoffice Theme** Sifr
- **Graphic Editor** GIMP

![](https://i.ibb.co/yFHgph6/gimp.png)

Unfortunately, Python 2 Support has been dropped in Debian 11.
My GIMP scripts collection mostly no longer works.

- **Printer Driver** CUPS + GutenPrint
- **Torrent Client** Transmission
- **Non-Free Drivers** Broadcom Bluetooth & Intel Wifi

## How I Set Up Debian Part I : Debian Expert Installer
1. I use Debian Minimal CD (377MB) without any Desktop Environment.
2. Burn it to USB like usual and boot it.
3. I use **Expert Install** instead of normal installer for some reason.

- I need two locale active. en_US and id_ID.
Normal installer does not have that option.
- Expert install has an option to enable sudo by default for the created user.
- Expert install has an option to generate specific Initrd which is faster
than generic Initrd.
- I dualboot with Windows, so my BIOS time needs to be set to localtime.
Expert installer has option to use BIOS clock as localtime.
On normal installer, the BIOS clock is treated as UTC.

4. The Debian expert installer is very intuitive and easy to follow
(by Linux standard). Just follow the steps appear on the screen.
5. After the installation is finised, detach the USB installer, then reboot.
It will be boot faster than Arch base installation. And even faster than Alpine.
Unsure about Void, the last time I use Void, I was still on 5400 RPM HDD.

## How I Set Up Debian Part II: Get Everything Back
1. Edit the `/etc/apt/sources.list` to enable the online repository.
```
deb http://deb.debian.org/debian bullseye main contrib non-free
deb http://deb.debian.org/debian-security/ bullseye-security main contrib non-free
deb http://deb.debian.org/debian bullseye-updates main contrib non-free
```
I don't enable translations and deb-src to make APT works faster.

2. Connect to the internet. Since I have not installed the wifi driver.
The easiest way to connect to the internet is by using my phone in USB Tethering
mode. Attach the phone then `sudo dhclient usb0`. `usb0` is my USB interface, can be
found using `ip a` command.
3. `sudo apt update && sudo apt upgrade`
4. `sudo apt install git ca-certificates --no-install-recommends`
5. Clone this git repository
`git clone --depth=1 https://github.com/addy-dclxvi/debian-bspwm-dotfiles`
6. Deploy the dotfiles
`cp -r debian-bspwm-dotfiles/. ~`
7. Get back the packages
`sudo sh ~/.local/bin/packages`
Every packages I use are available in the repository. No need self compiling.
8. Reboot and fix some problems.

## How I Set Up Debian Part III: Extra Steps
- Change the default shell to fish
`chsh addy -s /usr/bin/fish`
- Copy the xbacklight configuration from `Documents/Backup/etc/X11/xorg.conf.d/`
to its original location. Without it my backlight cannot be reduced.
- Copy `Documents/Backup/usr/share/polkit-1/actions/` to its original location.
Without it, Nautilus cannot mount my external drive.
- Copy `Documents/Backup/usr/share/slim/themes` to its original location.
Then enable the themes by editing `/etc/slim.conf`.
- (Optional) Copy fonts from Windows partition to reduce the chance of broken
layout in Libreoffice when opening *docx* and *xlsx* files.

![](https://i.imgur.com/oJDiOnA.png)

- Generate user dirs by running `xdg-user-dirs-update` in terminal.

- I have installed the hardware acceleration driver.
Firefox can use it by editing `layers.acceleration.force enabled`
in `about:config`
- I want Neovim to be my default CLI text editor. Can be set using
`sudo update-alternatives --config-editor` command.

## Notes
- The amount of packages is 1000+ due to Debian package splitting.
It looks less cool on Neofetch. But it's actually pull less package content than
distros without package splitting. For example I can install only Libreoffice
Writer and Calc only without full Libreoffice suite. It's not possible on Arch.

![](https://i.imgur.com/5AYpvvl.png)

My 9 years old ThinkPad X230 still works pretty well with Debian.

- I place my autostart files in `~/.xsessionrc`. I also use that file to export
environment variable like locality settings, path, and touchpad settings.
- `~/.local/bin/` is where I place the scripts. I export that location to my
`$PATH` using `~/.xsessionrc` file. So, instead of typing `~/.local/bin/launch`,
I only need to type `launch` to execute the Rofi launcher script.
- I use `nmtui` command in terminal to connect to wifi
(after the network manager and wifi driver installed)
- I use Bspwm window rules to make my opened programs more organized.
Workspace 1 for Terminal. Workspace 2 for Web. Workspace 3 for Files.
Workspace 4 for Office. Workspace 5 for Multimedia. And Workspace 6 for Settings.
- I have no dedicated Power Menu. So, I create some `*.desktop` files in
`~/.local/share/applications/` for shutdown, reboot, sleep, hibernate, logout,
and lock. They will appear in Rofi just like normal apps. Accesible on both
keyboard and mouse.
- `Documents/Backup/` folder contains backups of my files that actually placed in
`/`.
- My Wifi interface is `wlp3s0`. If you see it in any configurations file,
replace it with your own. For example in Polybar config. Wifi interface can be
found using `ip a` command.
- Installing Debian from minimal install could be harder than Installing Arch.
Due to lack of documentation. And not every Arch Wiki guide can be applied on
Debian because different package manager, package names, package versions
(package versions in Debian mostly too old), different installation method, etc.
- My screen resolution is only 1366x768,
probaby everything will looks so small if this configurations applied in a
larger screen resolution.
- I set Bspwm to disable the gaps when only one window is opened.
Because screen space is important.

## Keybinds
I use mouse a lot. So, I try to make my configurations comfortable to use on both
mouse and keyboard. And I try to make the essential keybinds can be used using
left hand only, but still easy to memorize.

- **Super + Enter** Launch terminal
- **Super + A** App launcher
- **Super + W** Launch Web Browser
- **Super + Shift + W** Launch Web Browser in Incognito mode
- **Super + E** Launch File Explorer
- **Super + Q** Quit Bspwm
- **Super + Backspace** Reload Bspwm
- **Super + C** or **Alt + F4** Close app
- **Super + Shift + C** Kill app
- **Super + F** Fullscreen mode, hit it again to back to normal mode
- **Super + H/V** Split horizontal / vertical
- **Super + R** Cancel split
- **Super + Space** Toggle between floating mode and tiling mode
- **Super + Shift + Arrow** Send window to another edge of the screen,
only works if there are two window or more in a workspace
- **Alt + Tab** Switch focus to next window, including floated window
- **Alt + Shift + Tab** Switch focus to previous window, including floated window
- **Super + Tab** Switch to next window even if they are in another workspace
- **Control + Alt + Left/Right** Switch to next / previous workspace
- **Super + 1-6** Switch to workspace number
- **Super + Shift + 1-6** Send focused window to other workspace
- **Super + Control + Arrow** Expand window size
- **Super + Alt + Arrow** Shrink window size
- **Alt + Shift + Arrow** Move floating window
- **Super + L** Lockscreen
- **PrtSc** Take Screenshot then preview using default image viewer
- **Alt + PrtSc** Screenshot of active window only
- **Ctrl + PrtSc** Draw a rectangle to determine screenshoted area
- **Super + Drag Left Mouse Button** Move floating window
- **Super + Drag Right Mouse Button** Resize window
- **Scroll Up/Down on Polybar Volume Module** Increase/decrease the volume
- **Left Click on Polybar Volume Module** Mute/Unmute the volume
- **Right Click on Polybar Window Title Module** Close the window

## Credits
- i3lock Blur script originally written by
[petvas](https://github.com/petvas/i3lock-blur/blob/master/lock.sh)
- I get the PulseAudio controller script from
[Yuune](https://github.com/Yuune)'s repository
- Vim Plug [original repository](https://github.com/junegunn/vim-plug)
- nvim-colorizer
[original repository](https://github.com/norcalli/nvim-colorizer.lua)
- Syntastic
[original repository](https://github.com/vim-syntastic/syntastic)
- Mu Complete [original repository](https://github.com/lifepillar/vim-mucomplete)
- Airline [original repository](https://github.com/vim-airline/vim-airline)
- One Dark colorscheme
[original repository](https://github.com/joshdick/onedark.vim)
- Geany One Dark
[original source](https://github.com/geany/geany-themes/pull/21/files)
- I get the wallpaper from Freepik,
LICENSE Free with Attribution.
[City vector created by GarryKillian](https://www.freepik.com/vectors/city)
[- www.freepik.com](www.freepik.com).

