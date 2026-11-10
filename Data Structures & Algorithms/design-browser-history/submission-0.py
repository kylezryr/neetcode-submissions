class BrowserHistory:

    def __init__(self, homepage: str):
        # backPages is stack
        self.backPages = []
        # frontPages is stack
        self.frontPages = []
        self.currentPage = homepage

    def visit(self, url: str) -> None:
        # put currentPage onto stack
        self.backPages.append(self.currentPage)
        # set currentPage to url
        self.currentPage = url
        # clear forward history
        self.frontPages = []

    def back(self, steps: int) -> str:
        steps = min(len(self.backPages), steps)

        for i in range(steps):
            self.frontPages.append(self.currentPage)
            backPage = self.backPages.pop(-1)
            self.currentPage = backPage

        return self.currentPage

    def forward(self, steps: int) -> str:
        steps = min(len(self.frontPages), steps)

        for i in range(steps):
            self.backPages.append(self.currentPage)
            frontPage = self.frontPages.pop(-1)
            self.currentPage = frontPage

        return self.currentPage


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)