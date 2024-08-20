import customtkinter
from customtkinter import CTkButton, CTkLabel, CTkEntry, CTkOptionMenu, CTkToplevel, CTkTextbox, CTkImage
from PIL import Image
import os
from classes import *
from data import data


def error_popup(message):
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imgs")
    error = customtkinter.CTkToplevel()
    error.geometry("400x200")
    error.title("ERROR")
    error.resizable(False, False)
    screen_width = error.winfo_screenwidth()
    screen_height = error.winfo_screenheight()
    x = (screen_width - 400) // 2
    y = (screen_height - 200) // 2
    error.geometry(f"+{x}+{y}")
    error_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "error.png")), size=(100, 100))
    error_label = customtkinter.CTkLabel(master=error, text="", image=error_image)
    error_label.configure(image=error_image)
    error_label.pack()
    error_text = message
    error_label = customtkinter.CTkLabel(master=error, text=error_text, wraplength=300,
                                         font=customtkinter.CTkFont(size=15))
    error_label.pack()
    CTkButton(master=error, text="RETRY", command=lambda: error_button_event()).pack(expand=True, pady=10,
                                                                                          padx=20)

    def error_button_event():
        error.destroy()


def success_popup(message):
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imgs")
    success = customtkinter.CTkToplevel()
    success.geometry("400x200")
    success.title("SUCCESS")
    success.resizable(False, False)
    screen_width = success.winfo_screenwidth()
    screen_height = success.winfo_screenheight()
    x = (screen_width - 400) // 2
    y = (screen_height - 200) // 2
    success.geometry(f"+{x}+{y}")
    success_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "success.png")), size=(100, 100))
    success_label = customtkinter.CTkLabel(master=success, text="", image=success_image)
    success_label.configure(image=success_image)
    success_label.pack()
    success_text = message
    success_label = customtkinter.CTkLabel(master=success, text=success_text, wraplength=300,
                                           font=customtkinter.CTkFont(size=15))
    success_label.pack()
    CTkButton(master=success, text="OK", command=lambda: error_button_event()).pack(expand=True, pady=10,
                                                                                    padx=20)

    def error_button_event():
        success.destroy()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.withdraw()
        self.revista = data()
        self.main_window()

    def main_window(self):
        self.main_window = customtkinter.CTkToplevel()
        self.main_window.title("ARTICLES MANAGEMENT")
        self.main_window.geometry("1000x500")
        self.main_window.resizable(False, False)
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        x = (screen_width - 1000) // 2
        y = (screen_height - 500) // 2
        self.main_window.geometry(f"+{x}+{y}")

        # Sidebar
        sidebar_frame = customtkinter.CTkFrame(self.main_window, width=140, corner_radius=0)
        sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.main_window.grid_rowconfigure(0, weight=1)
        logo_label = customtkinter.CTkLabel(sidebar_frame, text="SCIENTIFIC JOURNAL",
                                            font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        new_button = customtkinter.CTkButton(sidebar_frame, text="ADD ARTICLE", command=self.new_button_event)
        new_button.grid(row=1, column=0, padx=20, pady=10)
        pending_button = customtkinter.CTkButton(sidebar_frame, text="PENDING", command=self.pending_button_event)
        pending_button.grid(row=2, column=0, padx=20, pady=10)
        rejected_button = customtkinter.CTkButton(sidebar_frame, text="REJECTED", command=self.rejected_button_event)
        rejected_button.grid(row=3, column=0, padx=20, pady=10)
        marked_button = customtkinter.CTkButton(sidebar_frame, text="MARKED", command=self.marked_button_event)
        marked_button.grid(row=4, column=0, padx=20, pady=10)
        accepted_button = customtkinter.CTkButton(sidebar_frame, text="ACCEPTED", command=self.accepted_button_event)
        accepted_button.grid(row=5, column=0, padx=20, pady=10)
        authors_button = customtkinter.CTkButton(sidebar_frame, text="AUTHORS", command=self.authors_button_event)
        authors_button.grid(row=6, column=0, padx=20, pady=10)
        volumes_button = customtkinter.CTkButton(sidebar_frame, text="VOLUMES", command=self.volumes_button_event)
        volumes_button.grid(row=7, column=0, padx=20, pady=10)
        exit_button = customtkinter.CTkButton(sidebar_frame, text="EXIT", fg_color="#E70000", hover_color="dark red",
                                              command=self.exit_button_event)
        exit_button.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.show_articles = customtkinter.CTkScrollableFrame(master=self.main_window,
                                                              label_font=customtkinter.CTkFont(size=15, weight="bold"),
                                                              corner_radius=5, width=690, height=420)
        self.show_articles.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.show_articles.grid_columnconfigure(0, weight=1)
        self.show_articles.place(relx=0.62, rely=0.5, anchor=customtkinter.CENTER)

        self.pending_button_event()

    def clear_scrollable_frame(self):
        for widget in self.show_articles.winfo_children():
            widget.destroy()

    def load_articles(self, status, title):
        self.clear_scrollable_frame()
        self.show_articles.configure(label_text=title)
        articles = self.get_articles_by_state(status)
        for i, article in enumerate(articles):
            author_names = [f"{author.first_name} {author.last_name}" for author in article.authors]

            title_label = customtkinter.CTkLabel(self.show_articles, text=article.title,
                                                 font=customtkinter.CTkFont(size=15, weight="bold"))
            title_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            authors_label = customtkinter.CTkLabel(self.show_articles, text=", ".join(author_names),
                                                   font=customtkinter.CTkFont(size=12))
            authors_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            delete_button = CTkButton(self.show_articles, text="Delete",
                                      command=lambda a=article: self.delete_article(a))
            delete_button.grid(row=i, column=2, padx=10, pady=5)

            info_button = CTkButton(self.show_articles, text="Learn More",
                                    command=lambda a=article: self.show_article_info(a))
            info_button.grid(row=i, column=3, padx=10, pady=5)

    def delete_article(self, article):
        Article.articles.remove(article)
        self.pending_button_event()

    def show_article_info(self, article):
        status = article.status
        if status == "Pending review":
            self.show_pending_info(article)
        elif status == "Rejected":
            self.show_rejected_info(article)
        elif status == "Accepted with comments":
            self.show_commented_info(article)
        elif status == "Accepted for publication":
            self.show_accepted_info(article)

    def show_pending_info(self, article):
        self.info_article_window(article, "Pending review", 400, 750)

    def show_rejected_info(self, article):
        self.info_article_window(article, "Rejected", 400, 680)

    def show_commented_info(self, article):
        self.info_article_window(article, "Accepted with comments", 400, 750)

    def show_accepted_info(self, article):
        self.info_article_window(article, "Accepted for publication", 400, 750)

    def info_article_window(self, article, status, width, height):
        info_win = CTkToplevel(self.main_window)
        info_win.title(f"Article Information - {status}")
        info_win.geometry(f"{width}x{height}")
        info_win.resizable(False, False)
        screen_width = info_win.winfo_screenwidth()
        screen_height = info_win.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        info_win.geometry(f"+{x}+{y}")

        cover_path = article.cover if os.path.exists(article.cover) else "./covers/default.jpg"
        cover_image = CTkImage(Image.open(cover_path), size=(200, 300))

        cover_label = CTkLabel(info_win, text="", image=cover_image)
        cover_label.configure(image=cover_image)
        cover_label.pack(pady=10)

        CTkLabel(info_win, text=f"Title: {article.title}", font=customtkinter.CTkFont(size=15, weight="bold")).pack(
            pady=5)
        CTkLabel(info_win, text="Authors: " + ", ".join(
            [f"{author.first_name} {author.last_name}" for author in article.authors]),
                 font=customtkinter.CTkFont(size=12)).pack(pady=5)
        CTkLabel(info_win, text="Keywords: " + ", ".join(article.keywords), font=customtkinter.CTkFont(size=12)).pack(
            pady=5)
        CTkLabel(info_win, text="Abstract:", font=customtkinter.CTkFont(size=12)).pack(pady=5)
        CTkLabel(info_win, text=article.abstract, font=customtkinter.CTkFont(size=12), wraplength=350).pack(pady=5)

        if status == "Pending review":
            reject_button = CTkButton(info_win, text="Reject",
                                      command=lambda: self.change_article_status(article, "Rejected", info_win))
            reject_button.pack(pady=5)

            mark_button = CTkButton(info_win, text="Add Comments", command=lambda: self.add_comments(article, info_win))
            mark_button.pack(pady=5)

            accept_button = CTkButton(info_win, text="Accept", command=lambda: self.accept_article(article, info_win))
            accept_button.pack(pady=5)

        if status == "Accepted with comments":
            comments_label = customtkinter.CTkLabel(info_win, text="Comments:", font=customtkinter.CTkFont(size=12))
            comments_label.pack(pady=5)
            comments_text = ", ".join(article.comments)
            comments_textbox = customtkinter.CTkLabel(info_win, text=comments_text, font=customtkinter.CTkFont(size=12),
                                                      wraplength=350)
            comments_textbox.pack(pady=5)

            modify_button = CTkButton(info_win, text="Modify Article",
                                      command=lambda: self.modify_article(article, info_win))
            modify_button.pack(pady=10)

    def modify_article(self, article, info_win):
        info_win.destroy()

        modify_win = CTkToplevel(self.main_window)
        modify_win.title("Modify Article")
        modify_win.geometry("400x400")
        modify_win.resizable(False, False)
        screen_width = modify_win.winfo_screenwidth()
        screen_height = modify_win.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 400) // 2
        modify_win.geometry(f"+{x}+{y}")

        title_var = customtkinter.StringVar(value=article.title)
        keywords_var = customtkinter.StringVar(value=", ".join(article.keywords))
        abstract_var = customtkinter.StringVar(value=article.abstract)

        CTkLabel(modify_win, text="Title:").pack(pady=5)
        CTkEntry(modify_win, textvariable=title_var).pack(pady=5)

        CTkLabel(modify_win, text="Keywords (comma separated):").pack(pady=5)
        CTkEntry(modify_win, textvariable=keywords_var).pack(pady=5)

        CTkLabel(modify_win, text="Abstract (max 250 characters):").pack(pady=5)
        abstract_textbox = CTkTextbox(modify_win, width=350, height=100)
        abstract_textbox.insert("1.0", article.abstract)
        abstract_textbox.pack(pady=5)

        def save_changes():
            article.title = title_var.get()
            article.keywords = keywords_var.get().split(", ")
            article.abstract = abstract_textbox.get("1.0", "end-1c").strip()
            article.status = "Pending review"  # Update the status here
            success_popup("Article details updated successfully.")
            modify_win.destroy()
            self.pending_button_event()  # Reload the list of pending articles

        CTkButton(modify_win, text="Save Changes", command=save_changes).pack(pady=20)

        def change_article_status(self, article, new_status, info_win=None):
            article.status = new_status
            success_popup(f"Article {new_status.lower()} successfully.")
            if info_win:
                info_win.destroy()
            self.pending_button_event()

        def add_comments(self, article, info_win):
            info_win.destroy()
            comments_win = CTkToplevel(self.main_window)
            comments_win.title("Add Comments")
            comments_win.geometry("400x300")
            comments_win.resizable(False, False)
            screen_width = comments_win.winfo_screenwidth()
            screen_height = comments_win.winfo_screenheight()
            x = (screen_width - 400) // 2
            y = (screen_height - 300) // 2
            comments_win.geometry(f"+{x}+{y}")

            CTkLabel(comments_win, text="Enter comments separated by commas:",
                     font=customtkinter.CTkFont(size=12)).pack(pady=10)
            comments_textbox = CTkTextbox(comments_win, width=300, height=100)
            comments_textbox.pack(pady=10)

            def save_comments():
                comments = comments_textbox.get("1.0", "end-1c").strip().split(",")
                article.comments = [s.strip() for s in comments]
                article.status = "Accepted with comments"
                success_popup("Comments added successfully.")
                comments_win.destroy()
                self.pending_button_event()

            CTkButton(comments_win, text="Save", command=save_comments).pack(pady=20)

        def accept_article(self, article, info_win):
            info_win.destroy()
            volumes_win = CTkToplevel(self.main_window)
            volumes_win.title("Assign Volume")
            volumes_win.geometry("400x200")
            volumes_win.resizable(False, False)
            screen_width = volumes_win.winfo_screenwidth()
            screen_height = volumes_win.winfo_screenheight()
            x = (screen_width - 400) // 2
            y = (screen_height - 200) // 2
            volumes_win.geometry(f"+{x}+{y}")

            CTkLabel(volumes_win, text="Select a volume to assign the article:",
                     font=customtkinter.CTkFont(size=12)).pack(pady=10)

            vol_names = [vol.name for vol in self.journal.volumes]
            selected_volume = customtkinter.StringVar(value=vol_names[0] if vol_names else "")
            CTkOptionMenu(volumes_win, variable=selected_volume, values=vol_names).pack(pady=10)

            def assign_volume():
                selected_vol = selected_volume.get()
                for vol in self.journal.volumes:
                    if vol.name == selected_vol:
                        vol.articles.append(article)
                        article.status = "Accepted for publication"
                        success_popup("Article accepted and assigned to volume successfully.")
                        volumes_win.destroy()
                        self.pending_button_event()
                        break

            CTkButton(volumes_win, text="Assign", command=assign_volume).pack(pady=20)

    def new_button_event(self):
        self.new_article_window()

    def new_article_window(self):
        new_article_win = CTkToplevel(self)
        new_article_win.title("CREATE NEW ARTICLE")
        new_article_win.geometry("400x850")
        new_article_win.resizable(False, False)
        screen_width = new_article_win.winfo_screenwidth()
        screen_height = new_article_win.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 850) // 2
        new_article_win.geometry(f"+{x}+{y}")

        title_var = customtkinter.StringVar(value="")
        keywords_textbox = None
        abstract_textbox = None
        file_size_var = customtkinter.StringVar(value="")
        cover_path_var = customtkinter.StringVar(value="")

        existing_authors = Author.get_all_authors()
        author_names = [f"{author.first_name} {author.last_name}" for author in existing_authors]
        selected_authors_vars = [customtkinter.StringVar(value="") for _ in range(3)]

        CTkLabel(new_article_win, text="Title:").pack(pady=5)
        CTkEntry(new_article_win, textvariable=title_var).pack(pady=5)

        for i in range(3):
            CTkLabel(new_article_win, text=f"Author {i + 1}:").pack(pady=5)
            CTkOptionMenu(new_article_win, variable=selected_authors_vars[i], values=author_names).pack(pady=5)

        CTkLabel(new_article_win, text="Keywords (separated by commas):").pack(pady=5)
        keywords_textbox = CTkTextbox(new_article_win, width=250, height=100)
        keywords_textbox.pack(pady=5)

        CTkLabel(new_article_win, text="Abstract (max 250 characters):").pack(pady=5)
        abstract_textbox = CTkTextbox(new_article_win, width=250, height=100)
        abstract_textbox.pack(pady=5)

        CTkLabel(new_article_win, text="File Size (in KB):").pack(pady=5)
        CTkEntry(new_article_win, textvariable=file_size_var).pack(pady=5)

        CTkLabel(new_article_win, text="Cover File Name:").pack(pady=5)
        CTkEntry(new_article_win, textvariable=cover_path_var).pack(pady=5)

        def create_article():
            title = title_var.get()
            selected_authors = [var.get() for var in selected_authors_vars if var.get()]
            selected_authors_objects = [author for author in existing_authors if
                                        f"{author.first_name} {author.last_name}" in selected_authors]
            keywords = keywords_textbox.get("1.0", "end-1c").strip()
            abstract = abstract_textbox.get("1.0", "end-1c").strip()
            file_size = file_size_var.get()
            cover_path = f"./covers/{cover_path_var.get()}"

            if not title:
                error_popup("You must enter a title.")
                return
            if not selected_authors:
                error_popup("You must select at least one author.")
                return
            if not keywords:
                error_popup("You must enter keywords.")
                return
            if len(keywords.split(",")) > 5:
                error_popup("You can enter a maximum of five keywords.")
                return
            if not abstract:
                error_popup("You must enter an abstract.")
                return
            if len(abstract) > 250:
                error_popup("The abstract must not exceed 250 characters.")
                return

            new_article = Article(title, selected_authors_objects, keywords.split(","), abstract,
                                  int(file_size), status="Pending review", cover=cover_path)

            success_popup("Article created successfully.")
            new_article_win.destroy()
            self.pending_button_event()

        CTkButton(new_article_win, text="Create Article", fg_color="#28a745", hover_color="dark green",
                  command=create_article).pack(pady=20)

    def pending_button_event(self):
        self.load_articles("Pending review", "PENDING REVIEWS")

    def rejected_button_event(self):
        self.load_articles("Rejected", "REJECTED ARTICLES")

    def marked_button_event(self):
        self.load_articles("Accepted with comments", "ARTICLES WITH COMMENTS")

    def accepted_button_event(self):
        self.load_articles("Accepted for publication", "ACCEPTED ARTICLES")

    def authors_button_event(self):
        self.clear_scrollable_frame()
        self.show_articles.configure(label_text="AUTHORS")

        authors = Author.get_all_authors()

        current_row = 0
        for author in authors:
            author_label = customtkinter.CTkLabel(self.show_articles, text=f"{author.first_name} {author.last_name}",
                                                  font=customtkinter.CTkFont(size=15, weight="bold"))
            author_label.grid(row=current_row, column=0, padx=10, pady=5, sticky="w")
            current_row += 1

            articles_by_author = [article for article in Article.articles if author in article.authors]

            for article in articles_by_author:
                article_label = customtkinter.CTkLabel(self.show_articles, text=f"    {article.title}",
                                                       font=customtkinter.CTkFont(size=12))
                article_label.grid(row=current_row, column=0, padx=20, pady=5, sticky="w")

                delete_button = CTkButton(self.show_articles, text="Delete",
                                          command=lambda a=article: self.delete_article(a))
                delete_button.grid(row=current_row, column=1, padx=10, pady=5)

                info_button = CTkButton(self.show_articles, text="More info",
                                        command=lambda a=article: self.show_article_info(a))
                info_button.grid(row=current_row, column=2, padx=10, pady=5)

                current_row += 1

    def volumes_button_event(self):
        self.clear_scrollable_frame()
        self.show_articles.configure(label_text="VOLUMES")

        volumes = self.revista.volumes

        current_row = 0
        for volume in volumes:
            volume_name = volume.name
            article_count = len(volume.articles)
            unique_author_article_count = len(set([article.title for article in volume.articles]))

            volume_label = customtkinter.CTkLabel(self.show_articles,
                                                  text=f"{volume_name} - {article_count} articles ({unique_author_article_count} with unique authors)",
                                                  font=customtkinter.CTkFont(size=15, weight="bold"))
            volume_label.grid(row=current_row, column=0, padx=10, pady=5, sticky="w")
            current_row += 1

            for article in volume.articles:
                article_label = customtkinter.CTkLabel(self.show_articles, text=f"    {article.title}",
                                                       font=customtkinter.CTkFont(size=12))
                article_label.grid(row=current_row, column=0, padx=20, pady=5, sticky="w")

                delete_button = CTkButton(self.show_articles, text="Delete",
                                          command=lambda a=article: self.delete_article(a))
                delete_button.grid(row=current_row, column=1, padx=10, pady=5)

                info_button = CTkButton(self.show_articles, text="More info",
                                        command=lambda a=article: self.show_article_info(a))
                info_button.grid(row=current_row, column=2, padx=10, pady=5)

                current_row += 1

    def exit_button_event(self):
        self.quit()

    def get_articles_by_state(self, status):
        articles = []
        for article in Article.articles:
            if article.status == status:
                articles.append(article)
        return articles
