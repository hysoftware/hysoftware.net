import { Component } from '@angular/core';
import { MatTabsModule } from '@angular/material/tabs';

import { LinkListComponent } from '../link-list/link-list.component';
import { LegalZoneTable } from '../legal-zone-table/legal-zone-table';

@Component({
  selector: 'app-root',
  templateUrl: './root.component.html',
  styleUrl: './root.component.scss',
  imports: [MatTabsModule, LinkListComponent, LegalZoneTable]
})
export class RootComponent {

}
