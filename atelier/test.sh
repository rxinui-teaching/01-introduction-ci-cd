#!/bin/bash

test_h1_text(){
    echo -e "Test h1 text: \c";
    expected_result="Hello World of CI/CD";
    test_value=`grep "header-hello" ./index.html | cut -d ">" -f 2 | cut -d "<" -f 1`;
    return `test "$test_value" = "$expected_result"`;
}

test_h1_text && echo "OK" || (echo "KO" && exit 1);