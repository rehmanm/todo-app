using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using todo.Models;

namespace todo.Pages
{
    public class IndexModel : PageModel
    {
        private readonly todo.Models.TodoContext _context;

        public IndexModel(todo.Models.TodoContext context)
        {
            _context = context;
        }

        public IList<TodoItem> TodoItem { get;set; }

        public async Task OnGetAsync()
        {
            TodoItem = await _context.TodoItems.ToListAsync();
        }
    }
}
