import { integer, pgTable, serial, text, timestamp } from "drizzle-orm/pg-core";

export const posts = pgTable('posts', {
    id: serial('id').primaryKey(),
    createdAt: timestamp('created_at').defaultNow(),
})

export const comments = pgTable('comments', {
    id: serial('id').primaryKey(),
    createdAt: timestamp('created_at').defaultNow(),
    author: text('author').notNull(),
    body: text('body').notNull(),
    parent: integer('parent_id').notNull()
})

// We are intentionally not using a foreign key here, as the parent can be a post *or* a comment.
// Drizzle seemingly will only allow me to use a foreign key if the parent can only be one type.
// Maybe I'm just too new to the library. 
// I also lose the ability to ON DELETE CASCADE :(

export type DBPost = typeof posts.$inferSelect;
export type NewDBPost = typeof posts.$inferInsert;

export type DBComment = typeof comments.$inferSelect;
export type NewDBComment = typeof comments.$inferInsert;
