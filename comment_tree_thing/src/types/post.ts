import { PostgresJsDatabase } from 'drizzle-orm/postgres-js';
import { DBPost, NewDBPost, comments, posts } from '../db/schema';
import { sql } from 'drizzle-orm';
import { Comment } from './comment';

export class Post {
    constructor(
        public values: NewDBPost | DBPost,
        public children: Comment[] = [],
        private saved: boolean = false,
    ) {}

    get id() {
        return this.values.id;
    }

    addChild(child: Comment) {
        this.children.push(child);
    }

    async save(db: PostgresJsDatabase<Record<string, never>>) {
        try {
            const ret = await db
                .insert(posts)
                .values(this.values ?? {})
                .returning();
            this.values = ret[0];
        } catch (error) {
            console.log(error);
        }
        return this;
    }  

    async fetchComments(db: PostgresJsDatabase<Record<string, never>>) {
        try {
            const commentData = await db
                .select()
                .from(comments)
                .where(sql`${comments.parent} = ${this.values?.id}`)
                .execute();

            for (const data of commentData) {
                let comment = new Comment(data);
                comment = await comment.fetchChildren(db)
                this.addChild(comment);
            }

            return this;
        } catch (error) {
            console.log("this.values.id is null, can't fetch children")
            console.log(error);
        }
    }
}
