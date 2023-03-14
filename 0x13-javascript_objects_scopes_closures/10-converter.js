#!/usr/bin/node

exports.converter = (base) =>
{
    function newConverter(value) 
    {
        return value.toString(base);
    }
    return newConverter;
}