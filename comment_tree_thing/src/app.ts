import { db } from "./db/db";
import { Comment } from "./types/comment";
import { Post } from "./types/post";
import { getRandomCharacter } from "./utils/generate";

const post = await new Post({}).save(db)

const leftComment = await new Comment({
    author: getRandomCharacter(),
    body: "This is a comment",
    parent: post.id!
}).save(db)

const rightComment = await new Comment({
    author: getRandomCharacter(),
    body: "This is a controversial comment",
    parent: post.id!
}).save(db)

const leftleftComment = await new Comment({
    author: getRandomCharacter(),
    body: "I agree entirely.",
    parent: leftComment[0].id
}).save(db)

const leftrightComment = await new Comment({
    author: getRandomCharacter(),
    body: "I disagree.",
    parent: leftComment[0].id
}).save(db)

const rightleftComment = await new Comment({
    author: getRandomCharacter(),
    body: "Please never say that again.",
    parent: rightComment[0].id
}).save(db);

const leftleftleftComment = await new Comment({
    author: getRandomCharacter(),
    body: "something off topic!!! haha!! lol :p",
    parent: leftleftComment[0].id
}).save(db)

const comments = await post.fetchComments(db)
comments?.children.forEach(comment => comment.print())