using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using todo.Models;

namespace todo.Pages
{
    public class CreateModel : PageModel
    {
        private readonly todo.Models.TodoContext _context;

        public CreateModel(todo.Models.TodoContext context)
        {
            _context = context;
        }

        public IActionResult OnGet()
        {
            return Page();
        }

        [BindProperty]
        public TodoItem TodoItem { get; set; }

        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                return Page();
            }

            _context.TodoItems.Add(TodoItem);
            await _context.SaveChangesAsync();

            return RedirectToPage("./Index");
        }
    }
}