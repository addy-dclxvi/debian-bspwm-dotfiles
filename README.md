# Dotfiles

## Introduction
A repository contains backups of my Debian configurations to make myself easier to recreate my setup on a new OS install.

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

- **Terminal** Kitty
- **Compositor** Compton
- **GTK Theme** Materia-light
- **File Manager** Nautilus

![](https://i.imgur.com/PBNhpEy.png)

Usually I use Thunar.
But after Thunar migrated to GTK3, I feel it heavier.
I tried PCManFM and SpaceFM but did not feel comfortable.
So I try Nautilus, and it actually not heavy if runs without GNOME.
And with `--no-install-recommends` flag when installing.
It only pulls a small amount of GNOME dependencies,
just like Thunar pulls some XFCE dependencies.
Also, I have pulled GNOME desktop other component
like Evince, File Roller, GVFS, Pavucontrol, and GNOME Polkit anyway.

- **Archive Manager** File Roller
- **Icons** Faba
- **PDF Reader** Evince

![](https://i.imgur.com/XINPsbg.png)

I choose Evince because it has DJVU support out the box.
I can use it as ebook reader.

The Murder of Roger Ackroyd by Agatha Christie is one of the best book I ever read.
I still can't believe the ending. It can't be possible.
I have been tricked for 26 chapters.

- **Lock Screen** i3lock

![](https://i.imgur.com/5QaNc7i.png)

Clean sample without any without any window opened.

![](https://i.imgur.com/OAXaEW3.png)

Dirty example with some windows opened.
Not good for hiding sensitive image or video.

- **Web Browser** Firefox

![](https://i.imgur.com/1USbRal.png)

Nothing special here. Default config.

- **Hardware Acceleration Driver** i965-va-driver
- **Encoder/Decoder** ffmpeg
- **Media Player** MPV

![](https://i.imgur.com/WEo0CDK.png)

> Gentlemen, welcome to Arch Club.
> The first rule of Arch Club is you tell everyone you use Arch.
> The second rule of Arch Club is YOU HAVE TO TELL EVERYONE you use Arch!!
> Third rule of Arch Club, Someone yells "Install Gentoo!", goes limp, taps out,
> the install is over. Fourth rule, only one guy to an install.
> Fifth rule, one install at a time, fellas. Sixth rule, No YouTube tutorial,
> no blogger tutorial. Seventh rule, install will go on as long as they have to.
> And the eighth and final rule, If this is your first night at Arch Club,
> you have to install Arch!


![](https://i.imgur.com/E1nOJiE.png)

Steins;Gate

![](https://i.imgur.com/xM3YsVl.png)

Suckseed

![](https://i.imgur.com/NPGzAvy.png)

MPV can stream URL too.
In example above, I stream a YouTube video from Kurzgesagt channel.

- **Task Manager** HTOP

![](https://i.imgur.com/AM76LMf.png)

- **Power Manager** TLP
- **Image Viewer** Viewnior
- **Sound Mixer** PulseAudio
- **Policy Kit Frontend** Gnome Polkit
- **Notification Daemon** Dunst

![](https://i.imgur.com/LRpg6i9.png)

- **Pager** Less
- **CLI Shell** Fish

I have written an article about fish
(here)[https://addy-dclxvi.github.io/post/fish-shell/]

- **CLI File Manager** Ranger

![](https://i.imgur.com/gjbazp.pngJ)

- **CLI Image Viewer** Caca
- **CLI Text Editor** Neovim

![](https://i.imgur.com/8AVGrcH.png)

![](https://i.imgur.com/4deA5tS.png)

![](https://i.imgur.com/7brOSuK.png)

![](https://i.imgur.com/ZL25J8j.png)

I'm not a programmer. So my Neovim configuration is pretty simple,
centralized in `~/.config/nvim/init.vim`. Not many plugins installed.
Only statusline, syntax checker, auto completion, and hex code colorizer.

I save a copy of the plugins in this repo to make myself easier
to recreate my setup.
They are placed in `~/.config/nvim/*` and `~/.local/share/nvim*`.

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
- **Screenshooter** scrot
- **Wallpaper Handler** Hsetroot
- **Brightness Manager** xbacklight
- **Music Player** Cmus

![](https://i.imgur.com/dpr071F.png)

Tree/Library Mode (Num 1)

![](https://i.imgur.com/BGbSj5c.png)

Playlist Mode (Num 2)

![](https://i.imgur.com/LrPfkD1.png)

File Browser Mode (Num 5)

CMUS is a also good for online radio stream.
The artist and song title is displayed correctly.
I save a copy of online radio steam files in this repository,
in `~/Music` folder.

> *Why don't you use Spotify like normal people do?*

Because Spotify recommendation playlist is not designned for
Progressive / Extreme / Technical Death Metal fans.
Listening radio is better for music discovery.
I can find many underrated artists and songs from radio.

- **Spreadseet** Libreoffice Calc

![](https://i.imgur.com/eZ2kyl1.png)

- **Word Processor** Libreoffice Writer

![](https://i.imgur.com/UsWzYH1.png)

- **Graphic Editor** GIMP

![]([https://i.imgur.com/cGlUGDV.png)

Unfortunately, Python 2 Support has been dropped in Debian 11.
My GIMP scripts collection mostly no longer works.

- **Printer Driver** CUPS + GutenPrint

### How I Set Up Debian Part I : Debian Expert Installer
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
(by Linux standard). just follow the steps appear on the screen.
5. After the installation is finised, detach the USB installer, then reboot.
It will be boot faster than Arch base installation. And even faster than Alpine.
Unsure about Void, the last time I use Void, I was still on 5400 RPM HDD.

### How I Set Up Debian Part II: Get Everything Back
1. Edit the `/etc/apt/sources.list` to enable the online repository.
```
deb http://deb.debian.org/debian bullseye main contrib non-free
deb http://deb.debian.org/debian-security/ bullseye-security main contrib non-free
deb http://deb.debian.org/debian bullseye-updates main contrib non-free
```

3. Connect to the internet 
2. `sudo apt update && sudo apt upgrade`
3. `sudo apt install git ca-certificates --no-install-recommends`
4. Clone this git repository
`git clone --depth=1 https://github.com/addy-dclxvi/debian-bspwm-dotfiles`
5. Deploy the dotfiles
`cp -r debian-bspwm-dotfiles/. ~`
6. Get back the packages
`sudo sh ~/.local/bin/packages`
Every packages I use are available in the repository. No need self compiling.
7. Reboot and fix some problems.

### How I Set Up Debian Part III: Extra Steps
- Change the default shell to fish
`chsh addy -s /usr/bin/fish`
- Copy the xbacklight configuration from `Documents/Backup/etc/X11/xorg.conf.d/`
to its original location. Without it my backlight cannot be reduced.
- Copy `Documents/Backup/usr/share/polkit-1/actions/` to its original location.
Without it, Nautilus cannot mount drive.
- Copy `Documents/Backup/usr/share/slim/themes` to its original location.
Then enable the themes by editing `/etc/slim.conf`.
- (Optional) Copy fonts from Windows partition to reduce the chance of broken
layout in Libreoffice when opening *docx* and *xlsx* files.

![](https://i.imgur.com/oJDiOnA.png)

### Notes
- The amount of packages is 1000+ due to Debian package splitting.
It looks less cool on Neofetch. But it's actually pull less package content than
distros without package splitting. For example I can install only Libreoffice
Writer and Calc only without full Libreoffice suite. It's not possible on Arch.

![](https://i.imgur.com/5AYpvvl.png)

My 9 years old ThinkPad X230 still works pretty well with Debian.

- I places my autostart files in `~/.xsessionrc`
- `~/.local/bin/` is where I place the scripts. I export that location to my
`$PATH` using `~/.xsessionrc` file. So, instead of typing `~/.local/bin/launch`,
I only need to type `launch` to execute the Rofi launcher script.
