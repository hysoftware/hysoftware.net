import { Component } from '@angular/core';
import { LinkListComponent } from '../link-list/link-list.component';

@Component({
  selector: 'app-root',
  templateUrl: './root.component.html',
  styleUrl: './root.component.scss',
  imports: [LinkListComponent]
})
export class RootComponent {

}
