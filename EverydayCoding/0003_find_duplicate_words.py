from BenchmarkUtil import benchmark_util
NO_OF_SOLUTION = 2


def solution_01(s):
    all_words = s.lower().split(" ")
    dupes = []
    for idx in range(len(all_words)-1):
        if all_words[idx] in dupes:
            continue
        for j in range(idx + 1, len(all_words)-1):
            if all_words[idx] == all_words[j]:
                dupes.append(all_words[idx])
                break
    return dupes


def solution_02(s):
    all_words = s.lower().split(" ")
    words_list = {}
    for word in all_words:
        if word in words_list:
            words_list[word] += 1
        else:
            words_list[word] = 1
    duplicated_words = []

    for word in words_list:
        if words_list[word] > 1:
            duplicated_words.append(word)

    return duplicated_words


tests = ["nothing duplicated in this sentence", "the dog and the cat", "x one one two two three",
         "three times times times", """Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main idea. In this handout, we will refer to this as the “controlling idea,” because it controls what happens in the rest of the paragraph.

How do I decide what to put in a paragraph?
Before you can begin to determine what the composition of a particular paragraph will be, you must first decide on an argument and a working thesis statement for your paper. What is the most important idea that you are trying to convey to your reader? The information in each paragraph must be related to that idea. In other words, your paragraphs should remind your reader that there is a recurrent relationship between your thesis and the information in each paragraph. A working thesis functions like a seed from which your paper, and your ideas, will grow. The whole process is an organic one—a natural progression from a seed to a full-blown paper where there are direct, familial relationships between all of the ideas in the paper.

The decision about what to put into your paragraphs begins with the germination of a seed of ideas; this “germination process” is better known as brainstorming. There are many techniques for brainstorming; whichever one you choose, this stage of paragraph development cannot be skipped. Building paragraphs can be like building a skyscraper: there must be a well-planned foundation that supports what you are building. Any cracks, inconsistencies, or other corruptions of the foundation can cause your whole paper to crumble.

So, let’s suppose that you have done some brainstorming to develop your thesis. What else should you keep in mind as you begin to create paragraphs? Every paragraph in a paper should be:

Unified: All of the sentences in a single paragraph should be related to a single controlling idea (often expressed in the topic sentence of the paragraph).
Clearly related to the thesis: The sentences should all refer to the central idea, or thesis, of the paper (Rosen and Behrens 119).
Coherent: The sentences should be arranged in a logical manner and should follow a definite plan for development (Rosen and Behrens 119).
Well-developed: Every idea discussed in the paragraph should be adequately explained and supported through evidence and details that work together to explain the paragraph’s controlling idea (Rosen and Behrens 119).
How do I organize a paragraph?
There are many different ways to organize a paragraph. The organization you choose will depend on the controlling idea of the paragraph. Below are a few possibilities for organization, with links to brief examples:

Narration: Tell a story. Go chronologically, from start to finish. (See an example.)
Description: Provide specific details about what something looks, smells, tastes, sounds, or feels like. Organize spatially, in order of appearance, or by topic. (See an example.)
Process: Explain how something works, step by step. Perhaps follow a sequence—first, second, third. (See an example.)
Classification: Separate into groups or explain the various parts of a topic. (See an example.)
Illustration: Give examples and explain how those examples prove your point. (See the detailed example in the next section of this handout.)
5-step process to paragraph development
Let’s walk through a 5-step process for building a paragraph. For each step there is an explanation and example. Our example paragraph will be about slave spirituals, the original songs that African Americans created during slavery. The model paragraph uses illustration (giving examples) to prove its point.

Step 1. Decide on a controlling idea and create a topic sentence
Paragraph development begins with the formulation of the controlling idea. This idea directs the paragraph’s development. Often, the controlling idea of a paragraph will appear in the form of a topic sentence. In some cases, you may need more than one sentence to express a paragraph’s controlling idea. Here is the controlling idea for our “model paragraph,” expressed in a topic sentence:

Model controlling idea and topic sentence — Slave spirituals often had hidden double meanings.
Step 2. Explain the controlling idea
Paragraph development continues with an expression of the rationale or the explanation that the writer gives for how the reader should interpret the information presented in the idea statement or topic sentence of the paragraph. The writer explains his/her thinking about the main topic, idea, or focus of the paragraph. Here’s the sentence that would follow the controlling idea about slave spirituals:

Model explanation — On one level, spirituals referenced heaven, Jesus, and the soul; but on another level, the songs spoke about slave resistance."""]
results = [[], ["the"], ["one", "two"], ["times"], ['paragraphs', 'are', 'the', 'building', 'of', 'many', 'in', 'a',
                                                    'paragraph', 'is', 'group', 'and', 'ideas', 'sentences', 'what',
                                                    'paragraph.', 'as', 'or', 'single', 'sentence', 'that', 'do',
                                                    'determine', 'section', 'paper', 'for', 'some', 'can', 'be', 'one',
                                                    'main', 'idea.', 'this', 'will', 'refer', 'to', 'i', 'decide',
                                                    'put', 'you', 'begin', 'must', 'on', 'an', 'working', 'thesis',
                                                    'statement', 'your', 'idea', 'information', 'each', 'related',
                                                    'other', 'should', 'reader', 'there', 'between', 'like', 'seed',
                                                    'from', 'whole', 'process', 'all', 'about', 'into', 'begins',
                                                    'with', 'development', 'foundation', 'create', 'every',
                                                    'controlling', 'expressed', 'topic', 'idea,', '(rosen', 'behrens',
                                                    'follow', 'through', 'details', 'explain', 'paragraph’s',
                                                    'organize', '(see', 'something', 'by', 'topic.', 'how', 'step',
                                                    'examples', 'prove', 'example', 'explanation', 'our', 'slave',
                                                    'songs', '—', 'spirituals', 'writer', 'level,']]

for i in range(len(tests)):
    for sln_idx in range(1, NO_OF_SOLUTION + 1):
        curr_time = benchmark_util.get_current_time()
        result = eval("solution_0{}".format(sln_idx))(tests[i])
        elapse_time = benchmark_util.get_elapse_time(curr_time)
        # debug:
        print("SOLUTION: {} took {} nanoseconds to finish test '{}'.".format(sln_idx, elapse_time, tests[i]))

        assert result == results[i], \
            "Solution {} with test '{}' had wrong result '{}' - expecting '{}'".format("solution_0{}".format(sln_idx),
                                                                                       tests[i], result, results[i])

