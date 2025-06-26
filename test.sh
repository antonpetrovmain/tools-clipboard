#!/bin/bash
echo -n "foo" | xsel -b
sleep 1
echo -n "bar" | xsel -b
sleep 1
echo -n "zab" | xsel -b

