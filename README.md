# Advent of code - solved using an LLM

This repository documents how one can solve [Advent of Code 2024](https://adventofcode.com/2024) (AOC) using [git-bob](https://github.com/haesleinhuepf/git-bob-advent-of-code) and the Large Language Model (LLM) Claude-3.5-Sonnet from Anthropic.
After [solving AOC1 during a github issue discussion](https://github.com/haesleinhuepf/git-bob-playground/issues/137) I decided to approach all AOCs this year like this. 
Hence, I created a repository for only this. You find the discussions I had with the LLM and the resulting AOC solutions in the list of issues of in this repository.
As the submission times of question and answers are saved, we can later measure how long it took to solve the individal AOC puzzles.

* [AOC1](https://github.com/haesleinhuepf/git-bob-playground/issues/137): A long discussion with the LLM to figure out how to provide the input data.
* [AOC2](https://github.com/haesleinhuepf/git-bob-advent-of-code/issues/2)
* [AOC3](https://github.com/haesleinhuepf/git-bob-advent-of-code/issues/3)
* [AOC4](https://github.com/haesleinhuepf/git-bob-advent-of-code/issues/4)
* [AOC5](https://github.com/haesleinhuepf/git-bob-advent-of-code/issues/5)
* [AOC6](https://github.com/haesleinhuepf/git-bob-advent-of-code/issues/6)
* [AOC7](https://github.com/haesleinhuepf/git-bob-advent-of-code/issues/7), [2nd attempt](https://github.com/haesleinhuepf/git-bob-advent-of-code/issues/8), [3rd attempt](https://github.com/haesleinhuepf/git-bob-advent-of-code/issues/9): Multiple attempts were necessary because the human instructor did not manage to upload the input data properly.
* [AOC8](https://github.com/haesleinhuepf/git-bob-advent-of-code/issues/10)
* [AOC9](https://github.com/haesleinhuepf/git-bob-advent-of-code/issues/11)

## How this was done

When approaching the AOCs, I created an issue with the full text of the AOC and a statement where to find the input data (typically `aoc*.txt`). 
Then, I added the trigger `git-bob try to implement this.`
In case the solution was wrong, I copied over the error message, and asked `git-bob try again`. 
Once all AOCs are solved, I will add some statistics about how long it took to generate the code to solve the AOCs.
