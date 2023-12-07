import { PostgresJsDatabase } from 'drizzle-orm/postgres-js';
import { DBComment, NewDBComment, comments } from '../db/schema';
import { sql } from 'drizzle-orm';

export class Comment {
    constructor(
        public values: NewDBComment | DBComment,
        public parent: number | null = values.parent,
        public children: Comment[] = []
    ) {}

    get id() {
        return this.values.id;
    }

    addChild(child: Comment) {
        this.children.push(child);
    }

    async save(db: PostgresJsDatabase<Record<string, never>>) {
        return await db
            .insert(comments)
            .values(this.values)
            .returning();
    }

    async fetchChildren(db: PostgresJsDatabase<Record<string, never>>) {
        try {
            let childComments = await db
                .select()
                .from(comments)
                .where(sql`${comments.parent} = ${this.values.id}`)
                .execute();

            for (const child of childComments) {
                const childComment = new Comment(child);
                this.addChild(childComment);
                console.log(this.values.body)
                console.log(child.body)
                await childComment.fetchChildren(db);
            }

            return this;
        } catch (error) {
            console.log(error);
            throw new Error(`Failed to fetch children for ${this.id}, parent is ${this.parent ?? null}`)
        }
    }

    print(depth: number = 0) {
        const indent = '  '.repeat(depth);
        const { author, body } = this.values;
        console.log(`${indent}- ${author}: ${body}`);

        for (const child of this.children) {
            child.print(depth + 1);
        }
    }

}
