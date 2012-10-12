CC=gcc
CFLAGS=-Wall -g -O2 -std=c99
LDFLAGS=
PKGCONFIG=pkg-config
LIBS=$(shell $(PKGCONFIG) --libs gtk+-3.0 glib-2.0 gmodule-2.0) -lm
INCS=$(shell $(PKGCONFIG) --cflags gtk+-3.0 glib-2.0 gmodule-2.0)
NAME=cashflo

ifeq ($(CC), i686-pc-mingw32-gcc)
	LDFLAGS += -Wl,-subsystem,windows
endif

$(NAME): cashflo.c
	$(CC) ${CFLAGS} ${LDFLAGS} -o $(NAME) cashflo.c ${INCS} ${LIBS}

clean:
	rm -f $(NAME) $(NAME).exe
