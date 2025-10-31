---
layout: post
title: "AvantGarble"
date: "2025-10-31T21:33:53Z"
slug: "avant-garble"
math: true
tags: ["dada", "art", "chatbot", "language model"]
categories: ["art"]
description: "A Dadist Chatbot"
---

This project explores the use of a primitive language model to build a chatbot.
The chatbot responds to the users' inputs with a series of random words
similarly to what your phone's autocomplete. You can try it
[here](https://avant-garble-68750635052.europe-west1.run.app/).

![AvantGarble Chatbot Screenshot](/posts/avant-garble/screenshot.png)

The project is inspired by Dadaism, an art movement of the early 20th century
that embraced randomness and irrationality as a means of challenging traditional
artistic values. The chatbot embodies these principles by generating nonsensical
responses that defy logical interpretation.

The chatbot uses a simple Markov chain to generate text based on a corpus of
English text ([Blog Authorship
Corpus](https://huggingface.co/datasets/barilan/blog_authorship_corpus)).

The code is available [on GitHub](https://github.com/tito21/avant-garble-python).
