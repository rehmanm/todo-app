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
    public class DeleteModel : PageModel
    {
        private readonly todo.Models.TodoContext _context;

        public DeleteModel(todo.Models.TodoContext context)
        {
            _context = context;
        }

        [BindProperty]
        public TodoItem TodoItem { get; set; }

        public async Task<IActionResult> OnGetAsync(long? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            TodoItem = await _context.TodoItems.FirstOrDefaultAsync(m => m.Id == id);

            if (TodoItem == null)
            {
                return NotFound();
            }
            return Page();
        }

        public async Task<IActionResult> OnPostAsync(long? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            TodoItem = await _context.TodoItems.FindAsync(id);

            if (TodoItem != null)
            {
                _context.TodoItems.Remove(TodoItem);
                await _context.SaveChangesAsync();
            }

            return RedirectToPage("./Index");
        }
    }
}
