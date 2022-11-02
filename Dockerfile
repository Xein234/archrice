From archlinux/archlinux:base

RUN pacman -Syu --noconfirm --needed git make
RUN git clone https://github.com/Xein234/dotfiles /.dotfiles \
    && cd /.dotfiles \
    && git checkout systemDocker \
    && make -B fromChrootToPreGrub

# Run cd /.dotfiles \
#     && git checkout systemDocker \
#     && make rootUserConfig \
#     && make nonRootUserConfig

# RUN cd /.dotfiles \
#     && git checkout systemDocker

RUN cd /.dotfiles \
    && echo 4\
    && make rootUserConfig

RUN cd /.dotfiles \
    && echo 11\
    && make nonRootUserConfig

# RUN su xein \
#     && cd ~/.dotfiles \
#     && cat Makefile

# RUN sudo -u xein -- sh -c "cd ~/.dotfiles && make neovimpart2"

RUN sudo -u xein -- sh -c "cd ~/.dotfiles && make neovimpart4"

CMD ["zsh"]
