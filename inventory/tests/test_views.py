
def test_view(self):
        w = self.create_whatever()
        url = reverse("views.whatever")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, resp.content)