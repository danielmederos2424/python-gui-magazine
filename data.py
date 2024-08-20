from classes import *


def data():
    # Create authors
    author1 = Author("María", "Zapatero", "author1@example.com", "0000-0001-2345-6789")
    author2 = Author("Antonio", "Acedo", "author2@example.com", "0000-0002-3456-7890")
    author3 = Author("Science", "", "author3@example.com", "0000-0003-4567-8901")
    author4 = Author("Conversus", "", "author4@example.com", "0000-0004-5678-9012")
    author5 = Author("Science & Technology", "", "author5@example.com", "0000-0005-6789-0123")
    author6 = Author("Research and Science", "", "author6@example.com", "0000-0006-2314-8764")
    author7 = Author("Author", "Test", "author7@example.com", "0000-0007-9780-2321")

    # Create article summaries
    summary1 = ("Astronomy is a fascinating scientific discipline that studies celestial bodies and phenomena that "
                "are found beyond Earth's atmosphere. Since ancient times, humans have looked to the sky for answers "
                "about the origin and nature of the universe. Throughout history, astronomy has evolved from simple "
                "observations to the sophisticated technology of telescopes and space probes.")

    summary2 = ("Science is a continuous process of exploration, discovery, and understanding of the world around us. "
                "Through observation, experimentation, and logical reasoning, scientists seek to unravel the mysteries "
                "of nature, from the fundamental laws of the universe to the intricate details of life on Earth.")

    summary3 = ("Nanotechnology is a field of science and engineering focused on the manipulation and control of matter "
                "at an extremely small scale, at the level of atoms and molecules. By working at this nanometric scale, "
                "scientists can create materials with unique properties and develop innovative technologies with "
                "applications across a wide range of fields.")

    summary4 = ("Science and technology are two interrelated fields that have radically transformed the way we live, work, "
                "and interact. Science, through observation, experimentation, and analysis, seeks to understand the world "
                "around us, from the smallest components of matter to the vast reaches of the universe. This understanding "
                "translates into fundamental knowledge about nature and its laws, which in turn drives technological advancement.")

    summary5 = ("Artificial life is a fascinating field of science focused on the creation and study of synthetic biological "
                "systems that mimic characteristics of living organisms. By combining biology, computer science, engineering, "
                "and chemistry, researchers seek to understand the fundamental principles of life and develop new forms of "
                "artificial life with innovative applications.")

    # Create articles
    article1 = Article("Astronomy", [author1, author2], ["astronomy", "universe"], summary1, 100, "Accepted for publication", "./covers/cover5.jpg")
    article2 = Article("Science", [author3], ["science"], summary2, 200, "Accepted for publication", "./covers/cover6.jpg")
    article3 = Article("Nanotechnology", [author4], ["engineering", "atom"], summary3, 150, "Accepted for publication", "./covers/cover2.jpg")
    article4 = Article("Rise of Intelligent Machines: AI & Robotics", [author5], ["science", "technology"], summary4, 150, "Rejected", "./covers/cover4.jpg")
    article5 = Article("Artificial Life", [author6], ["artificial", "systems"], summary5, 150, "Pending review", "./covers/cover1.jpg")

    # Create volumes and add articles
    volume1 = Volume("Volume 1")
    volume1.add_article(article1)
    volume1.add_article(article2)

    volume2 = Volume("Volume 2")
    volume2.add_article(article3)

    volume3 = Volume("Volume 3")

    # Create scientific journal and add volumes
    journal = ScientificJournal()
    journal.add_volume(volume1)
    journal.add_volume(volume2)
    journal.add_volume(volume3)

    return journal
