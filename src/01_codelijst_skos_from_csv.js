'use strict';
import {  generate_skos } from 'maven-metadata-generator-npm';
import {
    ttl,
    nt,
    jsonld,
    csv
} from './utils/variables.js';
console.log = function() {}
generate_skos(ttl, jsonld, nt, csv);

