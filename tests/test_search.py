from playwright.sync_api import expect

def test_search_check(home):
    home.search_product("Brocolli")
    results= home.get_search_results()
    for item in results:
        assert "Brocolli" in item, f"Expected 'Brocolli' in search results, but got '{item}'"

def invalid_search_check(home):
    home.search_product("xyz")
    results= home.get_search_results()
    assert len(results)==0, f"Expected no results for 'xyz', but got {len(results)} items"