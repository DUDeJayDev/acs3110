# Modified Preorder Trees

**Instructions for selfhosting are at the bottom of this file.**

As a concept, the modified pre-order tree isn't any more than a... Modified Pre-Order Depth-First Search implementation. The shape of tree is what many developers think when they think "tree traversal". The tree doesn't balance, distribute data any specific way, it's just a tree. 

So many modern concepts are designed as trees, especially replies and comment sections. Think about it, a parent (post) has multiple children (comments) that in return have their own children (comments) that... you get the point.

## Pre-Order Searching

To understand a modified pre-order search, we need to understand a "traditional" pre-order search. [Brilliant.org](https://brilliant.org/wiki/traversals/) defines pre-order searching as "visiting the current node, and successively moving to the left until a leaf is reached, visiting each node on the way there. Once there are no more children on the left of a node, the children on the right are visited." 

Let's take a visual look at what that *actually* means. 

![](./assets/Sorted_binary_tree_ALL_RGB.svg)
*Credit: Wikimedia*

For this tree, we would visit the nodes in the following order:

- F, B, A, D, C, E, G, I, H

However, if we think of each node as a comment to a post (`F`) we could optimize the loading of our comments, and, with a little bit of *modified* logic, visit our nodes based on something like likes, or a timestamp, who posted it, or some weird heuristic of all three. 

## Modified Pre-Order Searching

For simplicities sake, let's assume we only want to consider a timestamp as our "deciding factor", we could choose to visit the nodes like this:

- F, B, G, A, D, C, E, I, H

Loading the oldest data/comments last keeps relevant conversation shown to the user first and can allow us to simulate faster page loads by deferring the older comments (`I`, `H`) to only load when they're scrolled into view (or, take a page from Reddit and have the user select "Show More Comments"). Loading this data without a Modified Pre-Order search without consideration to how it'll actually be displayed, or loading too much data (and recuring into comments the user will never read or see) results in higher database load on the server and sending a potentially large payload to a client with a slower internet connection may run the risk of effectively dosing them by spending their bandwidth.

## Building It

Jumping right into it, let's talk tech. 

This demo is a TypeScript app using [Drizzle](https://orm.drizzle.team) as an ORM. Since we're building comments and storing them to a database. Naturally, we need a schema:

https://github.com/DUDeJayDev/acs3110/blob/6686518369b9384e02d59a90d9f0f0f3e8f029cc/comment_tree_thing/src/db/schema.ts#L3-L14

`posts` acts as our root node, we don't *really* care about it so it's just an id and timestamp. 

`comments` acts as every other node. We want to try to give this one some personality, as well as an enforced `notNull` `parent`. Traditionally, with a database you would think to use a foreign key and do some JOINing but here it doesn't seem that we can. 

https://github.com/DUDeJayDev/acs3110/blob/6686518369b9384e02d59a90d9f0f0f3e8f029cc/comment_tree_thing/src/db/schema.ts#L16-L17

To avoid having the DB look like it's doing all of the magic or making it obvious that this is supposed to be a tree implementation, we had to go out of our way to make some pretty strange classes. Let's take a look at `Comment`, as it has all of the methods of `Post` just with lightly different logic.

`Comment` holds the `values`, as they are in the DB. `values` accepts a type of a `NewDBComment`, which is basically just `author`, `body`, and `parent` as the DB will decide the ID and Timestamp fields. Or a `DBComment` which is a `NewDBComment` with the `id` and `created_at` fields reqired. Comments also provides a `parent`, which can be an id of a `Post`, or a `Comment` and the `children`. 

Traditional implementations do not need the `children` field, however it helps make our visualization easier. I wanted to build the visualization top down, not bottom up. 

Within our app script, we create a blank post and write it to the DB to return it's ID. 

Then, with just that one post ID, we create 6 comments in a hopefully visually interesting method, saving them all to the DB as we go along. Finally, we use the `fetchComments` method to grab the `leftComment` and `rightComment` as children to the `post`, and mostly randomly append children to those comments, then the children from those comments. 

Through this modified implementation of a pre-order search, we're able to access and show comments and their children in any order we please. By simply changing the where clause or adding an `ORDER BY`, we control how the tree is navigated since we control how and which parents are accessed.

---

### Selfhoster?

Cool.

You'll need to clone this repo, run `npm i`, start the below PostgreSQL container, then run `npm run start`.

```
docker run -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```
