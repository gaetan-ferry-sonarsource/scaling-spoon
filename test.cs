using System.Net.Http;
using System.Web.Mvc;

public class ExampleController: Controller
{
    [HttpGet]
    public IActionResult ImageFetch(string location)
    {
        var t = Task.Run(async () =>
		{
			try {
				string responseBody = await client.GetStringAsync(location);
			} catch (HttpRequestException e)
			{
				Console.WriteLine("\nException Caught!");
				Console.WriteLine("Message :{0} ", e.Message);
			}
		});
		t.Wait();

        return Ok();
    }
}
