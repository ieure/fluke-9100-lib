# Fluke 9100 Program Library

This contains some helpful programs for the Fluke 9100.

## Transferring files to the 9100

The simplest method of getting these programs onto a physical 9100 is
to upload them via the serial port.  This is documented in section 6.7
of the Programmer’s Manual.

I’ve found that flow control doesn’t work well with USB serial
adapters, which results in dropped characters when the Fluke’s buffer
fills up.  The `pv(1)` command can be used to limit the send rate to
something the Fluke can handle:

```shell
$ pv -q -L 240 filename.tl1
```
